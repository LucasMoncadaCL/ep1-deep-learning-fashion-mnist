# Revisión técnica 02 - Entrega de Lucas

**Fecha:** 19-09-2026

**Objeto:** PR #2, Handoff 02 y experimentos E3--E5.

**Base revisada:** `origin/main` en `3bdb411fca14cfb374c691a6ea4204c7fc2ce4e7`.

**Cabeza revisada después de correcciones documentales:** `b1b0f32`.

**Veredicto:** `APPROVED_TECHNICAL`.

**Revisión humana requerida:** Ignacio Silva (`yvvvl`).

## Alcance de la revisión

La auditoría contrastó la entrega con la rúbrica oficial, la guía maestra, el Handoff 02 y los contratos aceptados del proyecto. Se revisaron:

- configuraciones E3, E4 y E5;
- código reutilizable y pruebas modificadas;
- notebook ejecutado y sus outputs;
- tablas y seis figuras comparativas;
- Decision Log, informe de Lucas y handoff a Cesar;
- reproducibilidad con `uv`, calidad automática y protección de `main`;
- ausencia de evaluación o predicción sobre test durante el ajuste.

## Riesgos examinados

1. modificación simultánea de variables;
2. selección basada en test;
3. métricas incompletas o incompatibles con la rúbrica;
4. configuración declarada pero no aplicada;
5. conclusiones más fuertes que la evidencia disponible;
6. resultados huérfanos o imposibles de reproducir;
7. handoff que presente una candidata como modelo final;
8. documentación contradictoria entre notebook, tablas e informes.

## Evidencia verificada

- Las pruebas aseguran que E3 cambia solo learning rate, E4 solo batch size y E5 solo capas ocultas respecto de su control.
- El notebook conserva seis celdas de código ejecutadas, cero errores y resultados para nueve configuraciones.
- Accuracy, Precision, Recall y F1 están presentes en variantes macro y ponderada.
- Las curvas son legibles y respaldan las interpretaciones sobre convergencia y gaps.
- La candidata `[256,128]` se presenta como compromiso y no oculta que `[512,256,128]` obtuvo mayor desempeño absoluto.
- `early_stopping=true` se rechaza hasta que exista un callback real y probado.
- El ejecutor predice exclusivamente sobre `X_val`; no se detectó evaluación ni predicción sobre test en E3--E5.
- `uv lock --check`, 22 pruebas y Ruff 0.16.8 finalizaron correctamente.
- El workflow `Calidad/pruebas-y-lint` pasó en GitHub.
- El informe LaTeX de Lucas compiló en tres páginas; todas fueron renderizadas e inspeccionadas sin defectos visuales.

## Hallazgos y resolución

### R02-01 - Redondeo discordante

La tabla consolidada mostraba Precision Macro y ponderada `0,8738` para `E3_lr_0_01`, mientras el notebook ejecutado mostraba `0,8737`.

**Resolución:** la tabla se alineó con el notebook versionado.

### R02-02 - Duración presentada como valor estable

Algunos textos usaban la proporción temporal `1,60` sin indicar que provenía de una corrida CPU específica, aunque la duración varía entre ejecuciones.

**Resolución:** las cifras se identifican como corrida de referencia y se declara que tiempo no es un criterio aislado. El notebook usa una conclusión cualitativa compatible con su ejecución visible.

### R02-03 - Informe formal ausente

La etapa tenía informe operativo Markdown, pero no una versión formal equivalente a la preparada para Ignacio.

**Resolución:** se incorporó `docs/latex/collaborators/lucas/main.tex`, junto con instrucciones de compilación, control de artefactos y revisión visual.

## Conclusión

No quedan hallazgos críticos ni importantes dentro del alcance de Lucas. La configuración candidata, sus trade-offs, limitaciones y condiciones de continuación están respaldados de forma suficiente para integrar la etapa y permitir que Cesar trabaje sobre un control explícito.

Este veredicto es técnico. El Handoff 02 permanece `READY_FOR_REVIEW` hasta que Ignacio complete la revisión cruzada y Lucas autorice la integración como dueño del repositorio.
