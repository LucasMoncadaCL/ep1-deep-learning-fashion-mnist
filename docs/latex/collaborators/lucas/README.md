# Informe formal de Lucas

`main.tex` presenta de forma formal la etapa E3–E5: ajuste de learning rate, batch size y capacidad, selección de una configuración candidata y decisión condicional sobre Early Stopping.

El documento complementa `docs/collaborators/lucas/REPORT.md`. El informe Markdown conserva la trazabilidad operativa y los comandos; el documento LaTeX está orientado a revisión académica y futura integración en el informe final.

Compilar desde esta carpeta con:

```powershell
New-Item -ItemType Directory -Force build | Out-Null
pdflatex -output-directory build main.tex
pdflatex -output-directory build main.tex
```

Las rutas a figuras son relativas al repositorio. Los tiempos corresponden a corridas CPU de referencia y pueden variar entre ejecuciones; las decisiones no dependen exclusivamente de ellos.

El 19-09-2026 la fuente se compiló dos veces con MiKTeX `pdflatex` y produjo un documento de tres páginas. Se renderizaron e inspeccionaron todas las páginas sin detectar texto cortado, solapamientos, tablas fuera de margen ni figuras ilegibles. El PDF de control permanece local; solo debe versionarse cuando forme parte de un entregable formal aprobado.
