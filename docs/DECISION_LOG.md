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
