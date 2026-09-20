# Política obligatoria de entorno

## 1. Regla del repositorio

Todo desarrollo local debe ejecutarse dentro de un entorno virtual `.venv` ubicado en la raíz del repositorio y creado mediante `uv venv`.

No se acepta como entorno reproducible:

- Python global;
- `python -m venv`;
- Conda;
- Poetry;
- un entorno virtual ubicado fuera del repositorio;
- instalar paquetes con `pip install` directamente;
- depender de paquetes que solo existen en el computador de un integrante.

Esta regla se aplica a Ignacio, Lucas y Cesar.

## 2. Creación del entorno

La versión oficial del proyecto es **Python 3.12.x**. El archivo `.python-version` fija la rama menor `3.12`; `uv` resolverá el parche estable disponible al crear el entorno.

Esta elección se basa en tres criterios:

- TensorFlow declara compatibilidad con Python 3.9–3.12;
- los runtimes actuales de Google Colab utilizan Python 3.12 (3.12.13 en el runtime 2026.07);
- fijar la rama menor mantiene compatibilidad entre colaboradores y permite recibir correcciones de parche sin migrar de versión de lenguaje.

Fuentes consultadas el 15-09-2026: [instalación oficial de TensorFlow](https://www.tensorflow.org/install/pip), [versiones de runtime de Google Colab](https://research.google.com/colaboratory/runtime-version-faq.html) y [gestión de Python con uv](https://docs.astral.sh/uv/concepts/python-versions/).

Desde la raíz del repositorio:

```powershell
uv venv --python 3.12 .venv
```

No se debe omitir `--python`. Para comprobar la versión resuelta:

```powershell
.\.venv\Scripts\python.exe --version
```

La salida debe comenzar con `Python 3.12.`.

### Validación inicial del repositorio

El 15-09-2026 se recreó correctamente `.venv` con `uv 0.11.8`; `uv` resolvió CPython 3.12.13. La validación posterior del bloque inicial actualizó el entorno a `uv 0.12.10` y CPython 3.12.14, con TensorFlow 2.21.0, NumPy 2.5.3, Pandas 3.0.5 y scikit-learn 1.9.1 declarados como dependencias directas en `pyproject.toml` y resueltos con versiones exactas en `uv.lock`. La etapa de Lucas volvió a reconstruir el entorno con `uv 0.11.8` y Python 3.12.13; las 22 pruebas automatizadas pasan, confirmando compatibilidad dentro de Python 3.12.x. Ruff 0.16.8 forma parte del grupo de desarrollo y se ejecuta mediante `uv run ruff`, sin depender de una versión flotante descargada por `uvx`.

### Activación en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Activación en Linux, macOS o Google Colab local equivalente

```bash
source .venv/bin/activate
```

La activación debe verificarse:

```powershell
python -c "import sys; print(sys.executable)"
```

La ruta mostrada debe apuntar a `.venv` dentro de este repositorio.

## 3. Instalación de dependencias

El manifiesto oficial ya es `pyproject.toml` y el bloqueo reproducible ya es `uv.lock`. `pyproject.toml` declara las dependencias de nivel superior sin fijar cada versión de tránsito; `uv.lock` registra las versiones exactas resueltas para reconstruir el mismo entorno. No se deben editar ni sustituir esas versiones manualmente.

El flujo oficial es:

```powershell
uv sync --frozen
```

Todo cambio permanente de dependencias deberá actualizar el manifiesto y el lock en el mismo cambio de Git. Las exploraciones temporales no deben alterar el entorno compartido ni instalarse con `pip` directo.

## 4. Comandos del proyecto

Los comandos documentados deben ejecutarse con el intérprete del entorno. Por ejemplo:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

No se aceptarán instrucciones que funcionen únicamente porque el Python global contiene paquetes adicionales.

## 5. Evidencia obligatoria por colaborador

Cada informe de colaborador debe registrar:

- salida de `uv --version`;
- salida de `python --version` dentro de `.venv`;
- ruta de `sys.executable`;
- comando usado para sincronizar o instalar dependencias;
- cualquier incompatibilidad encontrada;
- confirmación de que las pruebas se ejecutaron con `.venv`.

No es necesario copiar listas extensas de paquetes si ya existe un `uv.lock` versionado.

## 6. Archivos versionados y locales

| Elemento | Política |
|---|---|
| `.venv/` | Local, ignorado por Git |
| `.python-version` | Versionado; fija Python 3.12 |
| `pyproject.toml` | Versionado; declara dependencias de nivel superior |
| `uv.lock` | Versionado; fija las versiones resueltas y es obligatorio |
| caché global de uv | Local |
| comandos de reproducción | Versionados en README/documentación |

## 7. Colab

Colab no utiliza el `.venv` local. El notebook final de entrega presenta evidencia versionada y debe ejecutarse desde cero sin depender de rutas locales. Si se solicita reproducir validation en Colab, debe instalar versiones compatibles a partir del manifiesto del proyecto; no debe repetir F1 ni consultar test.

La validación en Colab no reemplaza la regla local de `uv venv`; comprueba portabilidad hacia el entorno de entrega.

## 8. CPU y GPU en Windows

Python 3.12 es válido para desarrollo local en Windows, pero TensorFlow moderno no ofrece GPU nativa de Windows. TensorFlow 2.10 fue la última versión con ese soporte; para TensorFlow 2.11 o superior, el uso de las GPU NVIDIA del equipo debe realizarse mediante **WSL2**. El desarrollo nativo de Windows puede utilizar CPU y sigue siendo suficiente para comprobaciones rápidas de Fashion-MNIST.

Esta distinción evita fijar una versión antigua de TensorFlow solo para conservar soporte GPU nativo. La misma versión de Python 3.12 debe utilizarse tanto en Windows como en WSL2.

## 9. Criterio de entorno listo

El entorno común estará listo cuando:

1. la versión de Python esté técnicamente justificada;
2. `.venv` pueda recrearse con `uv`;
3. las dependencias estén declaradas y bloqueadas;
4. las pruebas pasen usando el intérprete de `.venv`;
5. TensorFlow cargue correctamente;
6. la carga de Fashion-MNIST y el contrato de datos se ejecuten;
7. exista una ruta compatible para Colab.
