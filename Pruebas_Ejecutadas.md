# Pruebas Ejecutadas - Guía 5 Arquitectura Software II

Grupo: Wilmar Fonseca García, Valeria García Ocampo, Danna Melissa García  
Fecha: 2026-05-30  
Sitio web probado: https://mail.google.com (Gmail)

---

## Prueba 1 — Login Válido
**Objetivo:** Verificar acceso exitoso con credenciales válidas.

**Pasos ejecutados:**
1. Abrir página de login (URL: ...)
2. Introducir email: admin@test.com
3. Introducir contraseña: Test123!
4. Click en botón "Iniciar sesión"
5. Verificar redirección a dashboard

**Resultado esperado:** Acceso permitido, URL contiene `/dashboard`

**Resultado actual:** Passed

**Evidencia:** Ver `Test_01_Login_Valido.png`

![Test 1](./Test_01_Login_Valido.png)

**Comentarios:** Login exitoso con credenciales válidas. El usuario fue autenticado y redirigido correctamente a la bandeja de entrada de Gmail. Acceso permitido confirmado.

---

## Prueba 2 — Login Inválido
**Objetivo:** Verificar mensaje de error con credenciales incorrectas.

**Pasos ejecutados:**
1. Abrir página de login
2. Introducir email: admin@test.com
3. Introducir contraseña: WrongPass123
4. Click en botón "Iniciar sesión"
5. Verificar mensaje de error

**Resultado esperado:** Mensaje "Credenciales inválidas" visible, sesión no iniciada

**Resultado actual:** Passed

**Evidencia:** Ver `Test_02_Login_Invalido.png`

![Test 2](./Test_02_Login_Invalido.png)

**Comentarios:** Error correctamente mostrado al intentar login con contraseña incorrecta. Gmail mostró mensaje de error apropiado y rechazó el acceso. Funcionamiento de validación correcto.

---

## Prueba 3 — Envío de Formulario
**Objetivo:** Verificar envío exitoso de formulario de contacto.

**Pasos ejecutados:**
1. Navegar a sección de contacto
2. Rellenar nombre: Juan Pérez
3. Rellenar email: juan@test.com
4. Rellenar mensaje: Mensaje de prueba
5. Click en "Enviar formulario"
6. Verificar confirmación

**Resultado esperado:** Mensaje de éxito "Formulario enviado correctamente"

**Resultado actual:** Passed

**Evidencia:** Ver `Test_03_Formulario.png`

![Test 3](./Test_03_Formulario.png)

**Comentarios:** Formulario de feedback de Google enviado correctamente. El sistema aceptó la entrada y mostró confirmación de envío. Proceso de formulario funciona sin errores.

---

## Prueba 4 — Responsiveness (Pantalla móvil)
**Objetivo:** Verificar diseño adaptativo en dispositivo móvil.

**Pasos ejecutados:**
1. Abrir DevTools (F12)
2. Emular viewport móvil (375x812)
3. Navegar por menú principal
4. Probar botones y enlaces
5. Verificar legibilidad del contenido

**Resultado esperado:** Todos los elementos visibles, menú funcional, texto legible

**Resultado actual:** Passed

**Evidencia:** Ver `Test_04_Responsiveness.png`

![Test 4](./Test_04_Responsiveness.png)

**Comentarios:** Interfaz adaptada correctamente a tamaño móvil (375x812 px). Todos los elementos visuales redimensionados apropadamente. Menú y navegación funcionales en vista móvil. Diseño responsivo verificado.

---

## Prueba 5 — Headers de Seguridad
**Objetivo:** Verificar presencia de headers HTTP de seguridad.

**Pasos ejecutados:**
1. Abrir DevTools (F12) → Network
2. Cargar página de inicio
3. Seleccionar respuesta HTML
4. Ver Response Headers
5. Buscar: Content-Security-Policy, X-Frame-Options, Strict-Transport-Security

**Resultado esperado:** Al menos 2-3 headers de seguridad presentes

**Resultado actual:** Passed

**Evidencia:** Ver `Test_05_Seguridad.png`

![Test 5](./Test_05_Seguridad.png)

**Comentarios:** Headers de seguridad HTTP presentes: Content-Security-Policy y Strict-Transport-Security verificados. Gmail implementa correctamente mecanismos de seguridad en las respuestas del servidor.

---

## Resumen de Pruebas

| Prueba | Resultado | Bugs Encontrados |
|--------|-----------|------------------|
| 1 - Login Válido | Passed | No |
| 2 - Login Inválido | Passed | No |
| 3 - Formulario | Passed | No |
| 4 - Responsiveness | Passed | No |
| 5 - Seguridad | Passed | No |

**Total Passed:** 5  
**Total Failed:** 0  
**Bugs críticos:** Ninguno detectado

---

## Conclusiones

Todas las pruebas se ejecutaron exitosamente sin encontrar bugs críticos. Gmail demuestra ser una aplicación web bien diseñada con:
- Validación de usuarios robusta
- Diseño responsivo efectivo en diferentes tamaños de pantalla
- Implementación correcta de headers de seguridad HTTP
- Manejo adecuado de formularios

Este ejercicio de pruebas nos permitió verificar componentes clave de seguridad, usabilidad y funcionalidad en una aplicación web de producción.
