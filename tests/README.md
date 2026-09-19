# Tests y verificaciones

Este directorio alojará verificaciones pequeñas y enfocadas. Como mínimo se deben comprobar:

- formas, tipos y rangos después del preprocesamiento;
- separación sin solapamiento entre train, validation y test;
- salida del modelo con diez probabilidades por ejemplo;
- coherencia entre codificación de etiquetas, salida y loss;
- reproducibilidad razonable con una seed fija;
- carga correcta de configuraciones;
- generación de métricas y tablas con el esquema esperado.

Los tests no sustituyen el análisis experimental; protegen sus supuestos.

## Estado actual

`test_data_validation.py` cubre:

- aceptación de un split crudo válido y balanceado;
- rechazo de formas inesperadas;
- rechazo de imágenes que no sean `uint8`;
- rechazo de un rango crudo incompleto cuando se exige `[0, 255]`;
- rechazo de una distribución inesperada;
- aceptación de una partición train/validation completa y disjunta;
- rechazo de solapamiento entre train y validation;
- rechazo de particiones que omitan casos del conjunto de origen.
- normalización a `float32` en `[0, 1]` y codificación one-hot;
- repetibilidad del split estratificado con seed fija;
- construcción de E0 con 235.146 parámetros y diez probabilidades Softmax;
- coherencia de configuración entre salida Softmax, etiquetas one-hot y categorical crossentropy.
- cálculo explícito de Accuracy, Precision, Recall y F1 en sus variantes macro y ponderada.
- rechazo anticipado de tipos, rangos y estructuras inválidas en configuraciones.
- resumen de convergencia, costo y gaps a partir del historial de entrenamiento.
- construcción de un registro autocontenido con configuración, entrenamiento y métricas.
- control de que las configuraciones E3 modifiquen únicamente learning rate.
- control de que las configuraciones E4 modifiquen únicamente batch size respecto del control seleccionado en E3.

El total actual es 20 pruebas.

Ejecución:

```powershell
$env:PYTHONPATH = "src"
uv run python -m unittest tests.test_data_validation -v
```

La ejecución con Python global no es válida como evidencia del proyecto.
