# Entrega - Guía 5 (Borrador)

Portada:
- Nombre del proyecto: [Nombre]
- Integrantes: [Nombres y documento]
- Asignatura: Arquitectura de Software II
- Fecha: [YYYY-MM-DD]

1. Test Plan en Azure DevOps
- Crear un Test Plan en Azure DevOps > Test Plans > New Test Plan.
- Crear 5 Test Cases basados en `TestPlan_Azure.md` (Login válido, Login inválido, Formulario, Responsiveness, Seguridad).
- Ejecutar las pruebas manualmente, adjuntar capturas a cada caso y marcar resultado (Passed/Failed).
- Evidencias: carpeta `evidencias/tests/` con capturas de ejecución de cada test en la UI de Azure DevOps.

2. Archivo YAML (Azure Pipelines)
- Archivo añadido: `azure-pipelines.yml` en la raíz del repositorio.
- Explicación: Define un pipeline que se dispara en cada `push` a `main` o `develop`. Ejecuta instalación de dependencias, tests (si existen) y pasos de validación. Para mostrar el flujo en la entrega, incluye capturas de ejecución (logs de Azure Pipelines) y artefactos generados.

3. Disparador (Triggers / Commits)
- Requisito: Garantizar al menos 2 commits que disparen el pipeline en Azure DevOps.
- Evidencia: Capturas de la pestaña "Pipelines" > "Runs" mostrando las ejecuciones con los hashes/mesajes de commit.

4. Feedback (Retrospectiva individual)
- Para cada integrante incluya respuestas a:
  - ¿Qué hice bien?
  - ¿Qué hice mal?
  - ¿Cómo equipo, qué debemos seguir haciendo?

5. Estructura sugerida del PDF final
- Página 1: Portada con datos.
- Página 2: Índice.
- Páginas siguientes: Test Plan completo + evidencias.
- Sección: `azure-pipelines.yml` con captura de contenido y explicación de cada paso.
- Sección: Registro de commits y evidencias de ejecución en Azure DevOps Pipelines (capturas de "Runs").
- Sección final: Feedback individual y conclusiones.

Recomendación para generar el PDF final:
- Compilar en Word/LibreOffice o usar pandoc: `pandoc Entrega_Borrador.md -o Entrega_Final.pdf --pdf-engine=xelatex`
- Incluir imágenes en alta resolución desde la carpeta `evidencias/`.
- Estructura: Portada → Índice → Test Plan + evidencias → Pipeline YAML + runs → Feedback → Conclusiones.
