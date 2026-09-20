# Registro de decisiones - EP1 Fashion-MNIST

Este documento registra decisiones que afectan el diseño, la metodología o la coordinación del proyecto. Una decisión aceptada puede revisarse si aparece nueva evidencia; el cambio debe quedar documentado en una entrada posterior, sin reescribir retroactivamente la historia.

## Estados

- `propuesta`: todavía requiere validación.
- `aceptada`: vigente para el proyecto.
- `descartada`: evaluada y no adoptada.
- `reemplazada`: sustituida por una decisión posterior.

---

## D-001 - Selección de Fashion-MNIST

**Estado:** aceptada

**Origen:** acuerdo del equipo

**Evidencia futura:** descripción del dataset y análisis exploratorio del notebook

### Situación

La evaluación permite escoger un dataset de clasificación facilitado por el docente. Se necesita un problema compatible con una MLP y suficientemente expresivo para analizar errores y generalización.

### Decisión

Utilizar Fashion-MNIST.

### Justificación técnica

Las imágenes de 28 x 28 píxeles pueden representarse como vectores de 784 características para una red fully connected. Sus diez clases generan un problema multiclase manejable, pero con confusiones visuales útiles para interpretar métricas, matriz de confusión y errores por clase.

---

## D-002 - Guía maestra como documento vivo

**Estado:** aceptada

**Origen:** acuerdo del equipo

### Situación

La rúbrica exige ajustar el modelo de acuerdo con resultados experimentales. Una configuración técnica fijada como receta impediría reaccionar correctamente a la evidencia.

### Decisión

Usar `GUIA_MAESTRA_EP1_FashionMNIST.md` como marco metodológico y de coordinación, no como especificación inmutable del modelo final.

### Justificación técnica

Se mantendrán fijos los requisitos evaluativos y el protocolo experimental. Arquitecturas, hiperparámetros y técnicas concretas serán hipótesis sujetas a validación.

---

## D-003 - Baseline limpio y justificable

**Estado:** propuesta

**Origen:** hipótesis inicial

**Evidencia requerida:** ejecución E0 y comparación posterior

### Situación

Se necesita un punto de referencia común que permita medir el efecto de optimizadores, regularización y cambios de capacidad.

### Decisión propuesta

Comenzar con una MLP `[256, 128]`, activación ReLU, salida Softmax, categorical crossentropy, SGD, `learning_rate=0.01`, `batch_size=128`, 20 épocas y sin regularización.

### Justificación técnica

La red tiene capacidad moderada para aprender relaciones no lineales, pero evita incorporar desde el inicio técnicas cuyo aporte deberá medirse por separado. La configuración no se considera óptima hasta contar con evidencia.

---

## D-004 - Desarrollo local y validación final en Colab

**Estado:** aceptada

**Origen:** acuerdo del equipo

### Situación

El equipo dispone de GPU local y trabaja colaborativamente con Git, mientras que la pauta solicita un cuaderno en Google Colab.

### Decisión

Desarrollar y experimentar localmente en archivos `.ipynb`, versionar el trabajo con Git y ejecutar el notebook final de principio a fin en un entorno limpio de Google Colab antes de la entrega.

### Justificación técnica

El desarrollo local aprovecha el hardware disponible. La ejecución limpia en Colab valida portabilidad, dependencias, orden de celdas y cumplimiento del formato de entrega.

---

## D-005 - Grupo de tres integrantes

**Estado:** aceptada

**Origen:** autorización ya resuelta con el docente

### Situación

La pauta general menciona trabajo en parejas, pero el equipo está compuesto por Ignacio Silva, Lucas Moncada y Cesar Rojas.

### Decisión

Trabajar formalmente como grupo de tres, distribuyendo responsabilidades y manteniendo dominio integral del proyecto por parte de cada integrante.

### Justificación metodológica

La autorización administrativa está resuelta. La revisión cruzada y la preparación conjunta evitarán que la división de tareas fragmente el conocimiento requerido para la defensa.

---

## D-006 - Documentación obligatoria por colaborador

**Estado:** aceptada

**Origen:** acuerdo del equipo

### Situación

La división de tareas puede generar resultados difíciles de revisar o defender si las decisiones permanecen solo en conversaciones o notebooks personales.

### Decisión

Cada colaborador mantendrá un informe versionado con alcance, decisiones, configuraciones, evidencia, verificaciones, limitaciones y resumen de handoff.

### Justificación metodológica

La documentación individual conserva trazabilidad sin fragmentar el conocimiento. También permite verificar contribuciones y preparar la defensa individual exigida por la pauta.

---

## D-007 - Handoffs secuenciales con metas flexibles

**Estado:** aceptada

**Origen:** acuerdo del equipo

### Situación

El trabajo depende de contratos progresivos: los experimentos de hiperparámetros requieren datos y baseline estables; la evaluación final requiere una configuración candidata trazable.

### Decisión

Adoptar el flujo Ignacio -> Lucas -> Cesar. Cada etapa tiene metas orientativas y un criterio verificable de salida. Pueden añadirse pasos técnicamente justificados.

### Justificación metodológica

El orden reduce duplicación y cambios incompatibles. La flexibilidad evita convertir el plan en una receta que ignore evidencia nueva.

---

## D-008 - Material docente y artefactos pesados fuera de Git

**Estado:** aceptada

**Origen:** decisión de arquitectura

### Situación

Los PDF docentes, la rúbrica binaria, datasets, modelos y ejecuciones completas son material local o artefactos pesados que no deben sobrecargar el repositorio.

### Decisión

Ignorar esos archivos y versionar únicamente código, configuraciones, documentación técnica del proyecto, notebooks curados, tests y evidencia final seleccionada.

### Justificación técnica

Git debe preservar fuentes pequeñas y revisables. Datos y artefactos regenerables se obtienen mediante procedimientos documentados; las figuras y tablas que respaldan el informe sí se conservan.

---

## D-009 - Fuente y contrato verificable de Fashion-MNIST

**Estado:** aceptada

**Origen:** revisión del repositorio oficial y validación directa de los IDX

### Situación

El handoff inicial dependía de propiedades conocidas de Fashion-MNIST, pero todavía no existía evidencia local de integridad, distribución o ausencia de duplicados exactos.

### Decisión

Utilizar la API moderna `keras.datasets.fashion_mnist.load_data()` y proteger las propiedades oficiales mediante un contrato documental y validadores automatizados. El repositorio de Zalando se considera fuente del dataset y referencia de formato, no plantilla de implementación.

### Justificación técnica

Los archivos oficiales fueron verificados contra sus checksums y cabeceras IDX. La API de Keras evita mantener un loader propio, mientras que las validaciones explícitas detectan cambios accidentales de forma, tipo, rango, distribución o partición.

---

## D-010 - Entorno local obligatorio con uv

**Estado:** aceptada

**Origen:** regla del equipo

### Situación

El trabajo se realizará en varios computadores. Utilizar Python global o herramientas diferentes para crear entornos puede producir dependencias incompatibles y resultados difíciles de reproducir.

### Decisión

Todo desarrollo local utilizará `.venv` en la raíz del repositorio, creado mediante `uv venv`. Las dependencias se instalarán y sincronizarán exclusivamente mediante `uv`. `.venv` permanecerá fuera de Git; la versión de Python, el manifiesto y `uv.lock` se versionarán cuando hayan sido validados.

### Justificación técnica

Un único flujo de entorno reduce variaciones entre colaboradores, permite reconstruir dependencias y separa claramente el estado del proyecto de los paquetes globales del sistema.

---

## D-011 - Python 3.12 como versión oficial

**Estado:** aceptada

**Fecha:** 15-09-2026

### Situación

El entorno requería una versión común que fuera estable, ampliamente utilizada, compatible con TensorFlow y cercana al runtime de entrega en Google Colab.

### Decisión

El proyecto utilizará Python 3.12.x. `.python-version` fija `3.12` y cada colaborador creará `.venv` con `uv venv --python 3.12 .venv`. El parche puede actualizarse dentro de la rama 3.12; cualquier cambio de versión menor exige una nueva decisión.

### Justificación técnica

TensorFlow soporta Python 3.9–3.12 y los runtimes actuales de Colab utilizan Python 3.12. Fijar la rama menor reduce divergencias entre equipos y conserva correcciones de parche. No se eligió una versión antigua para habilitar GPU nativa en Windows: TensorFlow moderno requiere WSL2 para usar GPU NVIDIA en Windows, independientemente de que el proyecto sea liviano y pueda validarse por CPU.

### Fuentes

- [TensorFlow: instalación mediante pip](https://www.tensorflow.org/install/pip)
- [Google Colab: versiones de runtime](https://research.google.com/colaboratory/runtime-version-faq.html)
- [uv: versiones de Python](https://docs.astral.sh/uv/concepts/python-versions/)

### Evidencia de validación

El 15-09-2026, `uv 0.11.8` creó `.venv` con CPython 3.12.13. Las 8 pruebas automatizadas existentes pasaron usando el intérprete de ese entorno. Las versiones del stack científico se decidirán y bloquearán por separado.

---

## D-012 - Stack inicial bloqueado y carga reutilizable

**Estado:** aceptada

**Fecha:** 16-09-2026

### Situación

La primera etapa necesitaba un entorno reproducible, una única implementación de carga/preprocesamiento y una forma comprobable de construir E0 antes de ejecutar experimentos.

### Decisión

Versionar `pyproject.toml` y `uv.lock`; centralizar la preparación en `ep1_fashion_mnist.data` y la MLP en `ep1_fashion_mnist.model`. El stack resuelto inicialmente es TensorFlow 2.21.0, NumPy 2.5.3, Pandas 3.0.5 y scikit-learn 1.9.1 con Python 3.12.14.

### Evidencia

La carga efectiva mediante Keras validó los splits oficiales y el contrato. El código produce la partición estratificada 54.000/6.000 con seed 42 y las pruebas automatizadas pasan dentro de `.venv`. E0 se construye con 235.146 parámetros y salida de diez probabilidades; todavía no se ha entrenado ni evaluado sobre test.

---

## D-013 - Funciones de control posteriores a E1/E2

**Estado:** aceptada

**Fecha:** 16-09-2026

### Situación

Se debía comparar activaciones y función de pérdida sin modificar simultáneamente arquitectura, partición, optimizador, learning rate, batch size ni épocas.

### Decisión

Mantener ReLU en las capas ocultas y categorical crossentropy como control para los experimentos posteriores.

### Evidencia

Con seed 42 y las restantes condiciones de E0, ReLU obtuvo accuracy de validation 0,8722; Tanh 0,8643 y Sigmoid 0,7535. Con ReLU fija, categorical crossentropy obtuvo 0,8722 frente a 0,7370 de MSE. La tabla `results/tables/E1_E2_validation_comparison.md` y las figuras E1/E2 conservan los resultados. Esta decisión selecciona un control, no el modelo final y no utilizó test.

---

## D-014 - Learning rate candidato después de E3

**Estado:** aceptada

**Fecha:** 18-09-2026

### Situación

La etapa de Lucas debía comparar learning rates sin modificar arquitectura, activación, pérdida, optimizador, batch, épocas, partición ni seed.

### Decisión

Usar `learning_rate=0.1` como control para el experimento E4 de batch size. La decisión es provisional para la cadena de hiperparámetros y no selecciona el modelo final.

### Evidencia

Con 20 épocas, `0.001`, `0.01` y `0.1` obtuvieron respectivamente accuracy de validation 0,8053, 0,8722 y 0,8933; sus F1 Macro fueron 0,8034, 0,8726 y 0,8936. La duración fue comparable, entre 20,52 y 21,47 segundos por CPU. La mejora de `0.1` sobre `0.01` fue de 2,12 puntos porcentuales de accuracy.

### Riesgo y seguimiento

Con `0.1`, el gap final de accuracy fue 0,0298 y el de loss 0,0885; la mejor accuracy de validation apareció en la época 13 y la menor loss en la 18. E4 y E5 deberán comprobar si esta separación aumenta, y la etapa condicional de Early Stopping retomará estas curvas. El conjunto oficial de test permaneció sellado.

---

## D-015 - Batch size candidato después de E4

**Estado:** aceptada

**Fecha:** 18-09-2026

### Situación

Después de seleccionar `learning_rate=0.1`, la etapa E4 debía comparar batch sizes sin modificar arquitectura, activación, pérdida, optimizador, épocas, partición ni seed.

### Decisión

Mantener `batch_size=128` como control para el experimento E5 de capacidad. La decisión es provisional para la cadena de hiperparámetros y no selecciona el modelo final.

### Evidencia

Con 20 épocas, los batch sizes 32, 128 y 512 obtuvieron respectivamente accuracy de validation 0,8860, 0,8933 y 0,8745; sus F1 Macro fueron 0,8864, 0,8936 y 0,8771. Las duraciones por CPU fueron 57,46, 20,98 y 10,01 segundos. Batch 128 logró el mejor desempeño con costo intermedio.

### Alternativas y seguimiento

Batch 32 presentó gaps finales de accuracy y loss de 0,0534 y 0,2022, además de deterioro de `val_loss` después de la época 9, por lo que se descarta por costo y sobreajuste. Batch 512 fue el más rápido y mostró los menores gaps, pero perdió 1,88 puntos porcentuales de accuracy frente a 128; queda como alternativa si el costo computacional se vuelve prioritario. E5 deberá comprobar si cambiar la capacidad modifica la separación train-validation. El conjunto oficial de test permaneció sellado.

---

## D-016 - Capacidad candidata después de E5

**Estado:** aceptada

**Fecha:** 18-09-2026

### Situación

E5 debía comparar capacidad manteniendo fijos datos, funciones, optimizador, `learning_rate=0.1`, batch 128, 20 épocas y seed 42.

### Decisión

Entregar `[256, 128]` como arquitectura candidata equilibrada para la etapa de Cesar. Esta decisión no congela el modelo final y puede revisarse con evidencia posterior.

### Evidencia

Las arquitecturas `[64]`, `[256, 128]` y `[512, 256, 128]` utilizaron 50.890, 235.146 y 567.434 parámetros; obtuvieron accuracy de validation 0,8873, 0,8933 y 0,8990, y F1 Macro 0,8881, 0,8936 y 0,8989. La red grande mejoró 0,57 puntos porcentuales de accuracy frente a la candidata, pero usó 2,41 veces más parámetros, tardó 1,60 veces más en la corrida de referencia y aumentó los gaps finales a 0,0379 de accuracy y 0,1215 de loss. La duración puede variar entre ejecuciones y no se utiliza como criterio aislado.

### Alternativas y seguimiento

`[64]` queda como alternativa compacta y `[512, 256, 128]` como alternativa de desempeño absoluto. Cesar recibirá `[256, 128]` para estudiar optimizadores y regularización sin asumir que sea una arquitectura definitiva. El conjunto oficial de test permaneció sellado.

---

## D-017 - Early Stopping no activado en la etapa de Lucas

**Estado:** aceptada

**Fecha:** 18-09-2026

### Situación

El plan permitía incorporar Early Stopping solo si las curvas sin callback mostraban una oportunidad material de controlar sobreajuste o costo.

### Decisión

No ejecutar una comparación adicional con Early Stopping sobre la candidata actual. Cesar deberá reevaluar la técnica si sus cambios de optimizador o regularización alteran sustancialmente la convergencia.

### Evidencia

Para `[256, 128]`, la menor `val_loss` fue 0,3009 en la época 18 y la final fue 0,3015; la diferencia aproximada de 0,0006 no representa deterioro material. La mejor accuracy fue 0,8938 en la época 13 y la final 0,8933. Con un máximo de 20 épocas, detener en la época 18 aportaría un ahorro pequeño.

### Alcance

La decisión evita añadir un callback sin evidencia suficiente y no sostiene que Early Stopping sea inútil. Si una configuración posterior presenta deterioro sostenido, deberá compararse con y sin callback, documentando `monitor`, `patience`, `min_delta`, restauración de pesos y presupuesto máximo.

---

## D-018 - Rechazo explícito de Early Stopping no implementado

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

El esquema contenía el campo booleano `early_stopping`, pero el ejecutor no construía callbacks. Aceptar `true` habría permitido registrar una técnica que no se aplicaba realmente.

### Decisión

Mientras no exista una implementación completa, `validate_config` rechaza `early_stopping=true` mediante un error explícito. Las configuraciones actuales, todas con `false`, mantienen su comportamiento y resultados.

### Justificación técnica

Fallar anticipadamente preserva la correspondencia entre configuración efectiva y evidencia. Si Cesar encuentra justificación para Early Stopping, deberá implementar y probar el callback junto con `monitor`, `patience`, `min_delta`, máximo de épocas y restauración de pesos antes de aceptar una configuración activa.

---

## D-019 - Retuning separado para optimizadores adaptativos

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

E6 comparó SGD, RMSProp y Adam sobre la candidata `[256, 128]` con el mismo `learning_rate=0.1`, batch 128, 20 épocas, seed 42 y sin regularización. SGD obtuvo Accuracy de validation 0,8952 y F1 Macro 0,8954; RMSProp obtuvo 0,1985 y 0,0684; Adam obtuvo 0,4722 y 0,4166.

### Decisión

No declarar RMSProp ni Adam inferiores de forma global a partir de E6. Abrir E6b como comparaciones separadas de learning rate por optimizador, manteniendo cada optimizador, arquitectura, funciones, batch, épocas, seed y regularización constantes.

### Justificación técnica

E6 identifica el efecto de sustituir exclusivamente el optimizador bajo un presupuesto común. La degradación marcada de los adaptativos con `0.1` indica que esa escala puede no ser adecuada para ellos. Retunear learning rate dentro de E6 mezclaría dos variables; E6b conserva la trazabilidad necesaria para comparar el comportamiento inicial y el régimen ajustado.

### Evidencia

`results/tables/E6_optimizer_initial_comparison.md`, las figuras E6 y `notebooks/03_cesar_optimization_evaluation.ipynb`. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-020 - Control provisional después de E6b

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

E6b ajustó `learning_rate=0.001` por separado para Adam y RMSProp, manteniendo las restantes condiciones de E6. Adam recuperó Accuracy de validation 0,8912 y F1 Macro 0,8916; RMSProp obtuvo 0,8933 y 0,8929. SGD con `learning_rate=0.1` conservó 0,8952 y 0,8954, respectivamente.

### Decisión

Mantener SGD con `learning_rate=0.1` como control provisional para los experimentos de regularización E7-E9. La configuración no queda congelada ni se selecciona todavía como modelo final.

### Justificación técnica

SGD presenta la mayor Accuracy y F1 Macro de las tres configuraciones retuneadas y los gaps finales más bajos. RMSProp quedó cerca en Accuracy, por lo que la diferencia debe repetirse con seeds adicionales antes de F0 si la selección final sigue dependiendo de ella. La elección actual permite evaluar regularización contra un control explícito sin demorar el flujo ni confundir las variables.

### Evidencia

`results/tables/E6b_retuned_optimizer_comparison.md` y sus figuras comparativas. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-021 - Dropout 0,2 como control para Batch Normalization

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

E7 comparó la configuración SGD recibida con Dropout `0,0` y `0,2`, manteniendo fija arquitectura, funciones, learning rate, batch, épocas, seed, Batch Normalization y L2. Dropout `0,2` obtuvo Accuracy de validation 0,8997 y F1 Macro 0,8997 frente a 0,8952 y 0,8954 sin Dropout. Sus gaps finales de accuracy/loss fueron 0,0021 y 0,0135, frente a 0,0287 y 0,0851.

### Decisión

Mantener Dropout `0,2` como control para E8. Batch Normalization se comparará sobre esta configuración, manteniendo L2 en cero.

### Justificación técnica

La mejora conjunta de métricas y la reducción marcada de los gaps respaldan que el dropout empleado tras cada capa oculta favoreció la generalización en esta corrida. La selección no atribuye todavía efectos a combinaciones de regularizadores: E8 y E9 deben evaluar sus técnicas de manera controlada.

### Evidencia

`results/tables/E7_dropout_comparison.md` y sus figuras comparativas. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-022 - Batch Normalization desactivada para L2

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

Antes de E8 se modificó `build_mlp` para que los bloques con Batch Normalization tengan el orden `Dense lineal → BatchNormalization → activación → Dropout`, y se añadió una prueba que comprueba esa estructura. E8 comparó Batch Normalization OFF/ON sobre el control de E7 con Dropout `0,2` y L2 `0`.

### Decisión

Mantener Batch Normalization desactivada para E9. E8 con Batch Normalization OFF obtuvo Accuracy de validation 0,8997 y F1 Macro 0,8997; con la técnica activa obtuvo 0,8922 y 0,8911, además de gaps mayores.

### Justificación técnica

El orden implementado aplica la normalización antes de ReLU y evita declarar una técnica con comportamiento ambiguo. Bajo las condiciones controladas de E8, añadir Batch Normalization no compensó su costo adicional ni mejoró generalización. La decisión es contextual y no descarta la técnica en otros regímenes de aprendizaje.

### Evidencia

`results/tables/E8_batch_norm_comparison.md`, sus figuras comparativas y la prueba `test_batch_normalization_precedes_hidden_activation`. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-023 - L2 desactivada para decidir Early Stopping

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

E9 comparó L2 `0` y `1e-4` sobre el control con SGD, Dropout `0,2` y Batch Normalization apagada. Sin L2 se obtuvo Accuracy de validation 0,8997 y F1 Macro 0,8997; con L2 `1e-4`, 0,8967 y 0,8970. El gap de loss disminuyó levemente con L2, pero la loss incluye la penalización regularizadora.

### Decisión

Mantener `l2_strength=0` como control para decidir E10. No se incorporará L2 a menos que aparezca nueva evidencia después de evaluar el protocolo de Early Stopping.

### Justificación técnica

El control sin L2 presenta la mayor Accuracy y F1 Macro y ya tiene gaps pequeños debido a Dropout. La reducción marginal del gap de loss no compensa la pérdida de métricas ni permite interpretar la loss regularizada como un costo directamente equivalente.

### Evidencia

`results/tables/E9_l2_comparison.md` y sus figuras comparativas. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-024 - Early Stopping no implementado para la configuración seleccionada

**Estado:** aceptada

**Fecha:** 19-09-2026

### Situación

El control seleccionado con SGD, Dropout `0,2`, sin Batch Normalization y sin L2 alcanza su mejor validation accuracy y validation loss al final de las 20 épocas. El ejecutor rechaza explícitamente `early_stopping=true` porque el callback aún no está implementado.

### Decisión

No implementar ni ejecutar Early Stopping en esta etapa. Mantener el máximo de 20 épocas para la configuración que se congelará antes de test.

### Justificación técnica

No existe deterioro sostenido ni ahorro material de épocas que justifique ampliar el ejecutor y el contrato de callbacks. Activarlo sin una comparación interpretable agregaría complejidad sin evidencia de beneficio.

### Evidencia

Curvas y resúmenes de E7/E9. El conjunto oficial de test no fue evaluado ni utilizado para esta decisión.

---

## D-025 - Configuración congelada y estrategia de evaluación final

**Estado:** aceptada

**Fecha:** 19-09-2026

### Decisión

Congelar la configuración `F0_frozen_config`: MLP `[256, 128]`, ReLU, Softmax, categorical crossentropy, SGD con `learning_rate=0.1`, batch 128, 20 épocas, seed 42, Dropout `0.2`, sin Batch Normalization, L2 ni Early Stopping.

Se evaluará una única vez el modelo seleccionado que conserva el split 54.000/6.000, sin reentrenar con los 60.000 ejemplos oficiales.

### Justificación técnica

La configuración reúne la mejor evidencia disponible de validation. Las corridas canónicas disponibles favorecen mantener L2 apagada, mientras una revisión externa observó una diferencia marginal e inversión; por ello se adopta L2 cero como opción prudente, sin atribuirle estabilidad robusta entre entornos. Conservar el split permite evaluar el modelo cuya configuración y número de épocas fueron seleccionados sin convertir test en sustituto de validation.

### Evidencia y restricción

`configs/F0_frozen_config.json` y `results/tables/F0_frozen_protocol.md`. A partir de esta decisión no se ajustarán arquitectura, funciones, optimizador, hiperparámetros, regularización ni épocas después de observar test.

---

## D-026 - Registro de evaluación final única

**Estado:** aceptada

**Fecha:** 19-09-2026

La configuración congelada se evaluó una única vez sobre los 10.000 ejemplos oficiales de test. Alcanzó Accuracy 0,8838 y F1 Macro 0,8836. Las mayores dificultades se concentran en Shirt y en confusiones visualmente plausibles entre prendas superiores. Estos resultados se registran como evaluación final; no habilitan ajustes posteriores.

---

## D-027 - Fuente canónica y contrato de presentación de F1

**Estado:** aceptada

**Fecha:** 20-09-2026

### Decisión

La implementación canónica es exclusivamente el paquete bajo `src/ep1_fashion_mnist/`. El registro local de F1 ya evaluado es la única evaluación decisoria de test y queda versionado en `results/records/F1_final_evaluation_record.json`, vinculado al hash de `configs/F0_frozen_config.json`.

El notebook final de Colab clona esta rama y presenta configuraciones, tablas, figuras y el registro F1. Puede reproducir validación si se requiere, pero no debe entrenar F1, predecir ni evaluar sobre test.

### Justificación técnica

Una segunda consulta de test sería otra evaluación y no debe confundirse con la medición decisoria ya registrada. Centralizar la implementación evita que un notebook con un modelo alternativo produzca métricas no comparables o cambie decisiones como la selección del optimizador.

### Evidencia

`docs/FINAL_EVALUATION_CONTRACT.md`, `results/records/F1_final_evaluation_record.json`, `results/tables/R03_canonical_validation_reproduction.md` y `notebooks/EP1_FashionMNIST_FINAL.ipynb`.
