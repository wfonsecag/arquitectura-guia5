# Guía Rápida - Taller Guía 5 Arquitectura de Software II
**Equipo:** 3 compañeros | **Entorno:** Azure DevOps | **Fecha:** 2026-05-30

---

## 📋 Roles Sugeridos

| Rol | Responsabilidades |
|-----|-------------------|
| **Responsable QA/Test** | Crear Test Plan, ejecutar 5 pruebas, capturar evidencias |
| **Responsable CI/CD** | Configurar `azure-pipelines.yml`, hacer 2 commits, capturar ejecuciones |
| **Responsable Docs** | Compilar PDF, añadir portada, organizar evidencias |

---

## 🚀 Paso a Paso (orden recomendado)

### PASO 1: Clonar el Repo (Todo el equipo)
```powershell
cd C:\Proyectos  # O tu directorio
git clone https://dev.azure.com/<ORG>/<PROYECTO>/_git/<REPO_NAME>
cd <REPO_NAME>
git checkout main  # O tu rama principal
```

### PASO 2: Crear estructura de carpetas
```powershell
mkdir -Force "evidencias/tests"
mkdir -Force "evidencias/pipelines"
```

### PASO 3: Añadir `azure-pipelines.yml` (Responsable CI/CD)
- Descarga o copia el archivo `azure-pipelines.yml` a la raíz del repo (ya está en tu carpeta local).
- Si no está, crea uno en `<REPO_ROOT>/azure-pipelines.yml`.

**Ejemplo mínimo (si prefieres simplificar):**
```yaml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

steps:
  - script: echo "Hola, CI/CD en Azure DevOps"
    displayName: 'Run a one-line script'
  - script: |
      python --version || node --version || echo "No ejecutable detectado"
    displayName: 'Check environment'
```

### PASO 4: Hacer PRIMER COMMIT (Responsable CI/CD)
```powershell
git add .
git commit -m "feat: Agregar azure-pipelines.yml para CI/CD del proyecto"
git push origin main
```

**Evidencia:** Captura de pantalla de Azure DevOps > Pipelines > Runs (muestra la ejecución del pipeline).

### PASO 5: Crear Test Plan en Azure DevOps (Responsable QA)
1. En Azure DevOps web (dev.azure.com):
   - Ve a **Test Plans** (si no aparece, ve a **Project Settings** > **Test management** > habilita Test Plans).
   - Click en **+ New Test Plan**.
   - Nombre: `Guía 5 - Test Plan`.
   - Descripción: "Plan de pruebas para el proyecto Arquitectura Software II".

2. Crear un **Test Suite** dentro del Plan:
   - Click **+ New Test Suite** > **Static suite** > Nombre: "Pruebas Funcionales".

3. Crear 5 **Test Cases**:
   - Click **+ New Test Case** (5 veces). Rellena:

**Test Case 1: Login Válido**
- Title: "Verificar login con credenciales válidas"
- Description: "Inicia sesión con usuario/contraseña correctos"
- Steps:
  1. Abrir página de login
  2. Introducir usuario: `admin@test.com`
  3. Introducir contraseña: `Test123!`
  4. Click "Iniciar sesión"
  5. Verificar redirección al dashboard
- Expected: Acceso exitoso, URL contiene `/dashboard`
- Actual Result: *(Rellena al ejecutar)*
- Attachment: *(Añade captura aquí)*

*(Repite para Test Case 2-5 según `TestPlan_Azure.md`)*

### PASO 6: Ejecutar y capturar pruebas (Responsable QA)
1. En el Test Plan, selecciona un Test Case.
2. Click **Run** (o **Run for Web Application** si aplicable).
3. Ejecuta los pasos manualmente en el sitio web elegido.
4. Captura evidencias:
   - Toma **screenshots** de cada paso.
   - Guarda en `evidencias/tests/Test_01_Login_Valido.png`, etc.
5. Adjunta imágenes al Test Case:
   - En la UI, click **Attachment** > sube las capturas.
   - Marca **Passed** o **Failed** según resultado.

**Carpeta esperada:**
```
evidencias/
├── tests/
│   ├── Test_01_Login_Valido.png
│   ├── Test_02_Login_Invalido.png
│   ├── Test_03_Formulario.png
│   ├── Test_04_Responsiveness.png
│   └── Test_05_Seguridad.png
└── pipelines/
    ├── Pipeline_Run_01.png
    └── Pipeline_Run_02.png
```

### PASO 7: Hacer SEGUNDO COMMIT (Responsable CI/CD)
```powershell
git add -A
git commit -m "test: Completar structure y agregar script de test"
git push origin main
```

**Evidencia:** Captura de la segunda ejecución del pipeline en Azure DevOps.

### PASO 8: Compilar PDF Final (Responsable Docs)
1. Edita `Entrega_Borrador.md`:
   - Portada: Nombres, documento, grupo, fecha.
   - Section 1: Test Plan → copias las 5 pruebas y pegas las imágenes.
   - Section 2: YAML → copias contenido de `azure-pipelines.yml` y pegas capturas del pipeline.
   - Section 3: Commits → lista los 2 commits con hash y captura de **Pipelines > Runs**.
   - Section 4: Feedback individual → cada integrante responde (qué hizo bien, mal, qué seguir).

2. Genera PDF (opción A o B):

**Opción A: Usar Word/LibreOffice (manual, recomendado)**
- Copia `Entrega_Borrador.md` a Word/LibreOffice.
- Pega imágenes en alta resolución (png o jpg).
- Ajusta formato (fuentes, espacios, bordes).
- Exporta a PDF: File > Export as PDF.

**Opción B: Usar pandoc (automático)**
```powershell
# Instala pandoc:
choco install pandoc xelatex  # O descárgalo desde https://pandoc.org/

# Genera PDF desde Markdown:
pandoc Entrega_Borrador.md -o Entrega_Final.pdf --pdf-engine=xelatex
```

3. **Verifica PDF**: abre y comprueba que todo está legible y con imágenes.

### PASO 9: Subir a la plataforma
- Sube `Entrega_Final.pdf` en la plataforma del curso (BlackBoard/Moodle/etc).
- Verifica que esté correctamente subido y visible.

---

## ✅ Checklist Final

- [ ] Estructura carpetas (`evidencias/tests`, `evidencias/pipelines`) creada.
- [ ] `azure-pipelines.yml` en raíz del repo.
- [ ] Primer commit "feat: azure-pipelines.yml" → pipeline ejecutado.
- [ ] Test Plan creado en Azure DevOps con 5 Test Cases.
- [ ] 5 pruebas ejecutadas y capturadas en `evidencias/tests/`.
- [ ] Segundo commit con estructura → pipeline ejecutado nuevamente.
- [ ] Capturas de 2 ejecuciones pipelines en `evidencias/pipelines/`.
- [ ] PDF compilado y revisado.
- [ ] Feedback individual escrito en PDF.
- [ ] PDF subido a plataforma.

---

## 🎯 Notas Importantes

1. **Commits**: Asegúrate de que ambos commits pusheen a `main` o `develop` (rama configurada en el trigger del pipeline).
2. **Test Plan UI**: Si no ves "Test Plans" en Azure DevOps, pide permisos o ve a **Project Settings > Services > Test Management** (habilita si está desactivado).
3. **Propiedad intelectual**: Las capturas de pantallas y pruebas pertenecen al equipo; incluye nombres y documento en la portada.
4. **Tiempo estimado**: 2-3 horas (30 min setup, 1 hora pruebas, 1 hora PDF).

---

## 📞 Soporte Rápido

- Error: "Pipeline no se ejecuta" → Verifica que `azure-pipelines.yml` esté en la raíz y el trigger apunta a tu rama.
- Error: "No encuentro Test Plans" → Proyecto privado sin permisos; solicita acceso o cambia permisos en Project Settings.
- Error: PDF con imágenes borrosas → Usa imágenes PNG en mínimo 1920x1080 px.

---

**¿Listo? Empezad con PASO 1. ¡Adelante!**
