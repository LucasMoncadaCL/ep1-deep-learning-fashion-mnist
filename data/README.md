# Datos locales

Los archivos de datos no se versionan. Fashion-MNIST debe descargarse mediante el código del proyecto o recuperarse desde una fuente documentada y reproducible.

Este directorio puede contener localmente:

```text
data/raw/          fuentes sin modificar
data/processed/    transformaciones reproducibles
data/cache/        cachés descartables
```

Ningún notebook puede depender de una ruta absoluta del computador de un integrante. Toda transformación debe poder regenerarse desde código.
