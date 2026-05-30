# Test Plan - Sitio web (Ejemplo)

Proyecto: [Nombre del proyecto]
Responsable: [Nombre estudiante / grupo]
Fecha: [YYYY-MM-DD]

Objetivo: Ejecutar 5 pruebas funcionales y de usabilidad para identificar bugs en el sitio elegido.

Prueba 1 — Login válido
- Paso: Abrir la página de login, introducir credenciales válidas, enviar.
- Resultado esperado: Acceso exitoso y redirección al dashboard.
- Evidencia: Captura de pantalla del dashboard tras login.

Prueba 2 — Login inválido
- Paso: Introducir credenciales inválidas (usuario correcto, contraseña incorrecta), enviar.
- Resultado esperado: Mostrar mensaje de error claro y no iniciar sesión.
- Evidencia: Captura del mensaje de error.

Prueba 3 — Formulario de contacto / envío
- Paso: Completar campos obligatorios con datos válidos y enviar el formulario.
- Resultado esperado: Mensaje de éxito; datos recibidos en backend (si aplica).
- Evidencia: Captura de la confirmación y, si es posible, entrada registrada en consola/DB.

Prueba 4 — Comprobación de respuesta en móviles (responsiveness)
- Paso: Emular pantalla móvil (ej. 375x812) y navegar a la página principal y menú.
- Resultado esperado: Menú desplegable funcional, contenido legible y botones accesibles.
- Evidencia: Capturas en vista móvil y escritorio comparadas.

Prueba 5 — Seguridad básica / headers
- Paso: Revisar respuesta HTTP para headers de seguridad (Content-Security-Policy, X-Frame-Options, etc.) y probar acceso directo a recursos protegidos.
- Resultado esperado: Headers presentes; recursos protegidos no accesibles sin autenticación.
- Evidencia: Captura de la respuesta HTTP (herramientas devtools o curl).

Notas sobre evidencias:
- Para cada prueba guarda: descripción, pasos, fecha/hora, captura (imagen), explicación del resultado y si se considera bug, la severidad y acciones sugeridas.
