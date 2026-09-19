# Informe formal de Ignacio

`main.tex` es una versión formal y presentable de la etapa inicial. Sus valores provienen de las configuraciones, tablas y figuras versionadas; el registro operativo sigue siendo `docs/collaborators/ignacio/REPORT.md`.

Compilar desde esta carpeta con un motor LaTeX instalado:

```powershell
New-Item -ItemType Directory -Force build | Out-Null
pdflatex -output-directory build main.tex
pdflatex -output-directory build main.tex
```

El directorio `build/` y los auxiliares están ignorados por Git. En el equipo donde se preparó este bloque no se detectó `pdflatex` ni `latexmk`, por lo que se validó la fuente y sus rutas, pero no se generó un PDF local. El PDF solo debe versionarse tras una revisión formal.
