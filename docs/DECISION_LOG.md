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

Las arquitecturas `[64]`, `[256, 128]` y `[512, 256, 128]` utilizaron 50.890, 235.146 y 567.434 parámetros; obtuvieron accuracy de validation 0,8873, 0,8933 y 0,8990, y F1 Macro 0,8881, 0,8936 y 0,8989. La red grande mejoró 0,57 puntos porcentuales de accuracy frente a la candidata, pero usó 2,41 veces más parámetros, tardó 1,60 veces más y aumentó los gaps finales a 0,0379 de accuracy y 0,1215 de loss.

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
