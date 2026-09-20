# Notebooks

Convención propuesta:

```text
01_ignacio_data_baseline.ipynb
02_lucas_hyperparameters.ipynb
03_cesar_optimization_evaluation.ipynb
EP1_FashionMNIST_FINAL.ipynb
```

Los notebooks contienen narrativa, ejecución y evidencia; la lógica reutilizable debe vivir en `src/ep1_fashion_mnist/`.

## Estado actual

- `01_ignacio_data_baseline.ipynb`: bloque de datos, E0, E1 y E2.
- `02_lucas_hyperparameters.ipynb`: E3, E4 y E5; ejecutado localmente desde `.venv` y listo para revisión.
- `03_cesar_optimization_evaluation.ipynb`: integra E6–F1 como evidencia de solo lectura; no vuelve a entrenar ni consulta test.
- `EP1_FashionMNIST_FINAL.ipynb`: notebook autónomo de entrega; contiene datos, código, experimentos, gráficos, decisiones y F1. No depende de módulos, configuraciones, tablas ni figuras del repositorio y debe ejecutarse desde un runtime nuevo de Colab.

Reproducción del notebook de Lucas desde la raíz:

```powershell
uv sync --frozen
uv run jupyter nbconvert --to notebook --execute --inplace notebooks\02_lucas_hyperparameters.ipynb --ExecutePreprocessor.timeout=600
```

Reglas:

- no editar simultáneamente el notebook final;
- no versionar notebooks de prueba en `notebooks/sandbox/` o `notebooks/scratch/`;
- reiniciar el kernel y ejecutar todas las celdas antes de entregar un bloque;
- evitar resultados huérfanos que no indiquen configuración o experimento;
- el notebook final debe funcionar en Colab sin rutas locales.
- los notebooks locales deben usar un kernel asociado al `.venv` creado mediante `uv venv`;
- el nombre del kernel no reemplaza la comprobación de `sys.executable`.
