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
- validación de que dataset, forma de entrada y estrategia de split coincidan con el ejecutor real.
- rechazo explícito de Early Stopping mientras el callback no esté implementado.
- resumen de convergencia, costo y gaps a partir del historial de entrenamiento.
- construcción de un registro autocontenido con configuración, entrenamiento y métricas.
- control de que las configuraciones E3 modifiquen únicamente learning rate.
- control de que las configuraciones E4 modifiquen únicamente batch size respecto del control seleccionado en E3.
- control de que las configuraciones E5 modifiquen únicamente las capas ocultas respecto del control seleccionado en E4.

- control de que las configuraciones E6 modifiquen únicamente el optimizador respecto de la candidata recibida.
- control de que las configuraciones E6b modifiquen únicamente learning rate respecto de su optimizador de E6.
- control de que las configuraciones E7 modifiquen únicamente Dropout respecto del control SGD.
- control de que las configuraciones E8 modifiquen únicamente Batch Normalization respecto del control E7.
- control de que las configuraciones E9 modifiquen únicamente la fuerza L2 respecto del control E8.
- control de que las repeticiones modifiquen únicamente la seed y de que F0 preserve el control seleccionado y el presupuesto de test.
- validación del protocolo congelado y de las métricas finales sin volver a consultar test.

El total actual es 31 pruebas.

Ejecución:

```powershell
$env:PYTHONPATH = "src"
uv run python -m unittest tests.test_data_validation -v
```

La ejecución con Python global no es válida como evidencia del proyecto.
