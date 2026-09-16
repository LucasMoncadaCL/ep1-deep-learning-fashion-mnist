# Informes en LaTeX

Este directorio almacenará las fuentes de los informes formales del proyecto. Puede utilizarse para:

- el informe final consolidado;
- informes formales individuales de Ignacio, Lucas y Cesar;
- componentes compartidos, como portada, bibliografía, comandos, tablas y estilos.

Los documentos LaTeX complementan, pero no reemplazan, los archivos `docs/collaborators/<nombre>/REPORT.md`. Los `REPORT.md` mantienen la trazabilidad operativa, las decisiones y los handoffs; los documentos LaTeX se destinan a entregables formales y versiones presentables.

## Estructura propuesta

La estructura se creará a medida que existan documentos reales:

```text
docs/latex/
├── final/
│   ├── main.tex
│   ├── sections/
│   └── figures/
├── collaborators/
│   ├── ignacio/
│   ├── lucas/
│   └── cesar/
└── shared/
    ├── bibliography.bib
    └── commands.tex
```

No es obligatorio utilizar todas estas carpetas. Deben incorporarse únicamente cuando exista contenido que las justifique.

## Reglas

- versionar archivos fuente como `.tex`, `.bib`, estilos y recursos necesarios;
- evitar duplicar manualmente resultados que puedan generarse desde tablas o figuras versionadas;
- mantener rutas relativas y compilación reproducible;
- documentar el motor y el comando de compilación cuando se defina la plantilla;
- conservar los artefactos temporales de compilación fuera de Git;
- versionar un PDF final solamente cuando corresponda a un entregable revisado.
