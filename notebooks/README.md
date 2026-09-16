# Notebooks

Convención propuesta:

```text
01_ignacio_data_baseline.ipynb
02_lucas_hyperparameters.ipynb
03_cesar_optimization_evaluation.ipynb
EP1_FashionMNIST_FINAL.ipynb
```

Los notebooks contienen narrativa, ejecución y evidencia; la lógica reutilizable debe vivir en `src/ep1_fashion_mnist/`.

Reglas:

- no editar simultáneamente el notebook final;
- no versionar notebooks de prueba en `notebooks/sandbox/` o `notebooks/scratch/`;
- reiniciar el kernel y ejecutar todas las celdas antes de entregar un bloque;
- evitar resultados huérfanos que no indiquen configuración o experimento;
- el notebook final debe funcionar en Colab sin rutas locales.
- los notebooks locales deben usar un kernel asociado al `.venv` creado mediante `uv venv`;
- el nombre del kernel no reemplaza la comprobación de `sys.executable`.
