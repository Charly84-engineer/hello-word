# Lista de tareas en Python


Aplicacion sencilla de consola para guardar y organizar tareas en un archivo local.

## Requisitos

- Tener instalado Python 3.
- Abrir una terminal dentro de esta carpeta.

Puedes comprobar que Python esta instalado con:

```bash
python --version
```

## Como iniciar

Desde la carpeta del proyecto, ejecuta:

```bash
python script.py listar
```

Al principio aparecera `No tienes tareas pendientes.` porque todavia no hay tareas.

## Comandos disponibles

### 1. Agregar una tarea

Escribe `agregar` seguido del texto de la tarea entre comillas:

```bash
python script.py agregar "Estudiar Python"
```

El programa respondera algo como:

```text
Tarea 1 agregada.
```

### 2. Ver las tareas

Usa `listar` para mostrar todas las tareas:

```bash
python script.py listar
```

Ejemplo de resultado:

```text
1. [ ] Estudiar Python
2. [ ] Practicar Git
```

El numero de la izquierda es el identificador de cada tarea. `[ ]` significa pendiente y `[x]` significa completada.

### 3. Completar una tarea

Usa `completar` y escribe el identificador de la tarea:

```bash
python script.py completar 1
```

Despues, al listar las tareas, veras:

```text
1. [x] Estudiar Python
```

### 4. Eliminar una tarea

Usa `eliminar` y escribe el identificador:

```bash
python script.py eliminar 2
```

La tarea se borrara de la lista.

## Ejemplo completo

```bash
python script.py agregar "Comprar pan"
python script.py agregar "Leer documentacion de Git"
python script.py listar
python script.py completar 1
python script.py eliminar 2
python script.py listar
```

## Archivos del proyecto

- `script.py`: contiene el programa.
- `tareas.json`: guarda tus tareas automaticamente. Este archivo es local y no se sube a Git porque esta incluido en `.gitignore`.
- `README.md`: contiene esta documentacion.

No necesitas crear `tareas.json` manualmente: aparece despues de agregar la primera tarea.


se agrego la nueva rama de modificaciones para el proyecto de git y github
