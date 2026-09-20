"""Construcción y compilación consistente de MLPs para los experimentos."""

from collections.abc import Sequence


def build_mlp(
    hidden_layers: Sequence[int],
    *,
    hidden_activation: str = "relu",
    dropout: float = 0.0,
    batch_normalization: bool = False,
    l2_strength: float = 0.0,
    seed: int = 42,
):
    """Construye una MLP sin compilar; las opciones permiten experimentos controlados."""
    from tensorflow import keras

    if not hidden_layers or any(units <= 0 for units in hidden_layers):
        raise ValueError("hidden_layers debe contener al menos una cantidad positiva de neuronas")
    if not 0.0 <= dropout < 1.0 or l2_strength < 0.0:
        raise ValueError("dropout debe estar en [0, 1) y l2_strength no puede ser negativo")

    keras.utils.set_random_seed(seed)
    regularizer = keras.regularizers.l2(l2_strength) if l2_strength else None
    model = keras.Sequential(name="fashion_mnist_mlp")
    model.add(keras.layers.Input(shape=(28, 28), name="image"))
    model.add(keras.layers.Flatten(name="flatten"))
    for index, units in enumerate(hidden_layers, start=1):
        if batch_normalization:
            model.add(
                keras.layers.Dense(
                    units, activation=None, kernel_regularizer=regularizer,
                    name=f"hidden_{index}",
                )
            )
            model.add(keras.layers.BatchNormalization(name=f"batch_norm_{index}"))
            model.add(keras.layers.Activation(hidden_activation, name=f"activation_{index}"))
        else:
            model.add(
                keras.layers.Dense(
                    units, activation=hidden_activation, kernel_regularizer=regularizer,
                    name=f"hidden_{index}",
                )
            )
        if dropout:
            model.add(keras.layers.Dropout(dropout, seed=seed + index, name=f"dropout_{index}"))
    model.add(keras.layers.Dense(10, activation="softmax", name="classification"))
    return model


def compile_model(model, *, optimizer: str, learning_rate: float, loss: str):
    """Compila un modelo con accuracy, preservando una interfaz explícita por experimento."""
    from tensorflow import keras

    if learning_rate <= 0:
        raise ValueError("learning_rate debe ser positivo")
    optimizer_class = {"sgd": keras.optimizers.SGD, "adam": keras.optimizers.Adam,
                       "rmsprop": keras.optimizers.RMSprop}.get(optimizer.lower())
    if optimizer_class is None:
        raise ValueError(f"Optimizador no soportado: {optimizer}")
    model.compile(
        optimizer=optimizer_class(learning_rate=learning_rate), loss=loss,
        metrics=[keras.metrics.CategoricalAccuracy(name="accuracy")],
    )
    return model
