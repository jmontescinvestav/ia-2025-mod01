
## **📤 Probar el Push con el README**

Ahora ejecuta estos comandos para probar el push:

```bash
# 1. Ver el estado actual de Git
git status

# 2. Agregar el README.md al staging area
git add README.md

# 3. Hacer commit con mensaje descriptivo
git commit -m "docs: Agregar README principal del repositorio

- Información del curso y estructura
- Descripción de laboratorios
- Instrucciones de uso
- Información del autor"

# 4. Hacer push a GitHub
git push origin main

# 5. Verificar que se subió correctamente
git log --oneline -3