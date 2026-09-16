# Publicar el repositorio privado en GitHub

**Objetivo:** Crear el repositorio privado del proyecto en la cuenta correcta, publicar el estado verificado de `main` e invitar a los dos colaboradores indicados.
**Por qué se requiere planificación:** La operación crea estado externo, publica historial Git y envía invitaciones a cuentas de terceros.
**Aceptación:** El propietario autenticado debe ser `LucasMoncadaCL`; el nombre elegido no debe existir previamente; el repositorio debe quedar privado y con descripción en español; el commit inicial debe tener título y cuerpo en español; `main` debe apuntar al mismo commit local y remoto; `Cesitar16` y `yvvvl` deben recibir acceso de escritura o una invitación pendiente verificable. No se sobrescribirá ningún repositorio, no se forzará el push y se detendrá la operación si la identidad, los usuarios o la disponibilidad del nombre no coinciden.

### Resultado 1: Destino externo validado

- Trabajo: comprobar la sesión de GitHub CLI, la cuenta propietaria, la existencia de los colaboradores y la disponibilidad de `ep1-deep-learning-fashion-mnist`.
- Riesgos/preguntas abiertas: una sesión autenticada con otra cuenta, un nombre ya ocupado o una cuenta de colaborador inexistente detienen el flujo.
- Verificar: `gh auth status; gh api user; gh api users/Cesitar16; gh api users/yvvvl; gh repo view LucasMoncadaCL/ep1-deep-learning-fashion-mnist`

### Resultado 2: Estado local publicado de forma íntegra

- Trabajo: repetir las comprobaciones relevantes, crear un commit inicial completamente en español, crear el repositorio privado mediante `gh`, configurar `origin` y publicar `main` sin forzar.
- Riesgos/preguntas abiertas: si el commit o el push falla, se conserva el estado local y no se ejecutan operaciones de rebase, pull o force push.
- Verificar: `git status --short --branch; git log -1 --format=fuller; git remote -v; git rev-parse HEAD; git ls-remote origin refs/heads/main`

### Resultado 3: Metadatos y colaboradores confirmados

- Trabajo: comprobar privacidad, propietario, descripción, rama por defecto e invitaciones/acceso de `Cesitar16` y `yvvvl`.
- Riesgos/preguntas abiertas: si GitHub no permite conceder acceso inmediatamente, se acepta una invitación pendiente siempre que su destinatario y permiso sean verificables.
- Verificar: `gh repo view LucasMoncadaCL/ep1-deep-learning-fashion-mnist --json nameWithOwner,isPrivate,description,defaultBranchRef; gh api repos/LucasMoncadaCL/ep1-deep-learning-fashion-mnist/invitations`
