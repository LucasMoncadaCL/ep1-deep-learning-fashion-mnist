# Flujo de colaboración y handoffs

## 1. Propósito

El proyecto utiliza handoffs secuenciales para evitar que un colaborador entregue código sin contexto, justificación o evidencia reproducible. El handoff no limita la colaboración ni impide volver a etapas anteriores; define un punto verificable desde el cual el siguiente integrante puede continuar.

## 2. Orden inicial

```text
Ignacio Silva -> Lucas Moncada -> Cesar Rojas -> integración grupal
```

El orden puede revisarse si aparece un bloqueo real. Un cambio debe registrarse en `DECISION_LOG.md`.

## 3. Metas flexibles

Todos los handoffs establecen **metas mínimas y orientativas, ampliables con justificación técnica**; no son una lista exhaustiva ni inmutable.

Las metas asignadas describen el resultado mínimo esperado, no una frontera rígida ni el único trabajo autorizado. Un colaborador puede añadir, reorganizar o proponer pasos si:

1. responden una pregunta técnica relevante;
2. no usan test para ajustar decisiones;
3. mantienen control experimental;
4. no rompen contratos aceptados sin documentarlo;
5. dejan evidencia y justificación.

Si el cambio altera el alcance general, el protocolo experimental, un contrato aceptado o las responsabilidades de otro integrante, debe registrarse como asunto abierto y revisarse antes de adoptarlo como decisión del proyecto.

No se valora la cantidad de experimentos por sí misma.

## 4. Documentación obligatoria por colaborador

Cada integrante mantiene un informe en `docs/collaborators/<nombre>/REPORT.md`. Antes de cerrar su etapa debe incluir:

- alcance realizado y cambios respecto del plan;
- archivos creados o modificados;
- decisiones técnicas y alternativas descartadas;
- experimentos ejecutados con sus IDs;
- configuraciones exactas;
- métricas, tablas o figuras relevantes;
- comandos o pasos de reproducción;
- verificaciones realizadas y su resultado;
- limitaciones, problemas y resultados negativos;
- asuntos abiertos para el siguiente colaborador;
- resumen de handoff.

Cada colaborador también debe demostrar que trabajó dentro del `.venv` creado con `uv`, según `docs/ENVIRONMENT.md`.

Una captura de pantalla o una cifra sin configuración no constituye evidencia suficiente.

## 5. Estados del handoff

- `NOT_STARTED`: definido, pero todavía no habilitado.
- `READY_TO_START`: entradas suficientes para comenzar.
- `WAITING_ON_PREDECESSOR`: depende del handoff anterior.
- `IN_PROGRESS`: trabajo activo.
- `READY_FOR_REVIEW`: entregables y documentación listos.
- `CHANGES_REQUESTED`: revisión encontró elementos pendientes.
- `ACCEPTED`: otra persona reprodujo o revisó la evidencia mínima.
- `BLOCKED`: existe un impedimento explícito y documentado.

El siguiente colaborador puede explorar en paralelo, pero no debe construir decisiones definitivas sobre una interfaz o baseline cuyo handoff no esté `ACCEPTED`.

## 6. Criterio general de salida

Una etapa está lista cuando:

1. comandos y pruebas se ejecutaron dentro del `.venv` creado con `uv`;
2. el código relevante está fuera del notebook cuando es reutilizable;
3. el notebook se ejecuta desde un kernel limpio;
4. las configuraciones tienen identificadores inequívocos;
5. las conclusiones distinguen evidencia de hipótesis;
6. no se utilizó test para ajustar;
7. el informe del colaborador está completo;
8. el handoff enumera entradas, salidas y decisiones abiertas;
9. el revisor puede explicar y continuar el trabajo.

## 7. Revisión cruzada

```text
Cesar revisa a Ignacio
Ignacio revisa a Lucas
Lucas revisa a Cesar
```

El revisor no certifica que el modelo sea óptimo. Certifica que el trabajo es comprensible, reproducible y suficientemente respaldado para continuar.

La revisión cruzada no reemplaza la aprobación del dueño del repositorio. Lucas revisa además que cada handoff respete el alcance global y autoriza su integración; ambas funciones deben quedar diferenciadas para evitar que un colaborador figure como único revisor de su propia entrega.

Cuando exista una auditoría técnica asistida, su evidencia y veredicto se registran en `docs/reviews/`. Esta auditoría complementa la revisión cruzada humana: puede aprobar técnicamente una entrega o solicitar cambios, pero no satisface por sí sola la aprobación externa exigida para integrar a `main`.

### Protección efectiva de `main`

GitHub aplica estas condiciones antes de integrar cambios en `main`:

- la PR debe estar actualizada respecto de `main`;
- el check `pruebas-y-lint` debe finalizar correctamente;
- debe existir al menos una aprobación de una persona distinta de quien realizó el último push;
- las conversaciones de revisión deben estar resueltas;
- no se permiten force-push ni eliminación de la rama.

Estas reglas también se aplican al dueño del repositorio. La protección automatiza el mínimo verificable, pero no sustituye la revisión de alcance ni la justificación técnica exigida por este documento.

## 8. Actualización de handoffs posteriores

Los handoffs de Lucas y Cesar comienzan como guías orientativas. El colaborador anterior debe completarlos con:

- commit o estado exacto desde el que continuar;
- configuración seleccionada como control;
- rutas de módulos y notebooks relevantes;
- resultados que deben reproducirse;
- riesgos conocidos;
- decisiones todavía abiertas.
