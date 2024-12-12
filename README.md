# Gestión de tareas
El aplicativo cumple con la administración y gestión de tareas en donde el usuario pueda crear, eliminar, actualizar, exportar e importar tareas.

## Librerías
El proyecto esta desarrollado usando `StreamLit`, usa como Base de Datos a `SQLalchemy`.

Para ejecutar el aplicativo se puede de manera local usando el comando streamliy run ./src/main.py o ejecutarlo en la nube por medio de GitHub.

**Se proyectan algunas muestras del aplicativo:**

![alt text](img/image.png)

![alt text](img/image-1.png)

![alt text](img/image-2.png)

![alt text](img/image-3.png)

![alt text](img/image-4.png)


## Aclaraciones:

Dentro de la carpeta img se encuentran las imágenes necesarias para cargar el README.md y una captura del resultado de usar `SonnaScanner` en el proyecto.

El proyecto original fue desarrollado en un entorno virtual en donde se instaló las dependencias necesarias, razón por la que existe un archivo “”requirements.txt“” en donde se encuentran las dependencias usadas para el proyecto.


### Desarrollo

Lo primero fue la creación y estructuración del main.py, importando las librerías necesarias para el desarrollo de `frontend`¨

Lo siguiente fue la creación de la vista qué verá el usuario, en donde se usó los tabs de StreamLit para tener pestañas en donde se listan las tareas, para agregar tarareas y para exportar o importar las tareas.

Se creó una especie de `backend` con SQLalchemy usando como Bases de Datos a `sqllite` en donde sé instancia la clase tarea con atributos como id, título, descripcion y estado.

Se crearon las funciones necesarias para consultas como listar todas las tareas, agregar una tarea, actualizar una tarea y eliminar una tarea. Me pareció curioso como por medio de SQLalchemy se abstraen muchas funciones o comandos que normalmente uno usaría para hacer una consulta directa de SQL.

En el main se probó que las funciones hicieran lo correcto y se empezaron a implementar en las vistas para darle funcionalidad a cada botón o pestaña.

Por medio de columnas en la pestaña de listar, se construyo una tabla en donde el usuario pueda ver todas sus tareas y el poder marcar o desmarcar una como completada. Le agrego que si en caso de estar desmarcada aparezca en pendiente y cuando se marque, aparezca como completa.

Tuve inconvenientes al implementar el actualizar o eliminar porque al hacer dicha acción no se actualiza o veía reflejado inmediatamente en la tabla, había que actualizar manualmente. Investigué un poco más en la documentación de StreamLiy y con ayuda de IA, fui capaz de que se actualizara luego de hacer cambios o eliminar.

Lo siguiente fue el agregar tareas, tuve el mismo problema que con marcar una tarea o eliminar, no se mostraban los cambios. Cosa que pude solucionar implementando algo parecido con la anterior ventana, con la diferencia de que al momento de enviar quedarán vacíos los campos para agregar otra tarea.

Por último, y el que más problemas me dio fue el exportar e importar. La verdad era mi primera vez trabajando con Python y no tenía muchos conocimientos con los diccionarios y el manejo de JSON, pero con ver algunos videos y preguntar a la IA fui capaz de hacer el exportar sin problemas.

Cabe mencionar que cree otro archivo para crear funciones que justamente se encargaran de exportar extrayendo las tareas de la BD e importando desde un JSON.

En el momento de hacer el importar tuve serios problemas con los cambios o actualizaciones en el listar, los mensajes parpadeaban y se colapsaba la página con el tiempo. Pude darme cuenta de que el problema era en como estaba usando la función `rerun()` de StreamLit que se llama constantemente al mostrar los mensajes, haciendo que la página colapsara por el alto número de mensajes. Una vez que corregí eso, el aplicativo funciono como se esperaba.



