# practica3-flask

# Operaciones con Estructuras de Datos en Python

Este proyecto contiene una API simple en Flask para realizar operaciones con diccionarios, conjuntos y tuplas en Python.

## Requisitos previos

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

# Además, necesitarás instalar Flask. Puedes hacerlo utilizando pip, el gestor de paquetes de Python:


"Ejecutando la aplicación
Para ejecutar la aplicación, sigue estos pasos:

Abre una terminal en el directorio donde se encuentra el archivo app.py.

# Ejecuta el siguiente comando para iniciar el servidor de desarrollo de Flask:


# flask run
Abre un navegador web y visita la dirección http://127.0.0.1:5000/ para ver la documentación de la API.

Operaciones disponibles
Operaciones con Diccionarios
Obtener el diccionario actual

# Ruta: /get_diccionario
Método: GET
Descripción: Devuelve el diccionario actual como JSON.
Agregar una clave-valor al diccionario

# Ruta: /agregar_clave_valor/<clave>/<valor>
Método: GET
Descripción: Agrega una clave y su valor al diccionario.
Eliminar una clave del diccionario

# Ruta: /eliminar_clave/<clave>
Método: GET
Descripción: Elimina una clave específica del diccionario.
Modificar el valor de una clave en el diccionario

# Ruta: /modificar_valor/<clave>/<nuevo_valor>
Método: GET
Descripción: Modifica el valor de una clave en el diccionario.
Combinar dos diccionarios mediante parámetros de consulta

# Ruta: /combinar_diccionarios
Método: GET
Descripción: Combina el diccionario actual con otro diccionario proporcionado en los parámetros de consulta.
Operaciones con Conjuntos
Agregar un elemento a un conjunto

# Ruta: /agregar_elemento_conjunto/<elemento>
Método: GET
Descripción: Agrega un elemento al conjunto.
Eliminar un elemento de un conjunto

# Ruta: /eliminar_elemento_conjunto/<elemento>
Método: GET
Descripción: Elimina un elemento específico del conjunto.
Combinar dos conjuntos mediante parámetros de consulta

# Ruta: /combinar_conjuntos
Método: GET
Descripción: Combina dos conjuntos proporcionados en los parámetros de consulta.
Obtener la diferencia entre dos conjuntos mediante parámetros de consulta

# Ruta: /diferencia_entre_conjuntos
Método: GET
Descripción: Calcula la diferencia entre dos conjuntos proporcionados en los parámetros de consulta.
Operaciones con Tuplas
Agregar un elemento a una tupla y crear una nueva tupla

# Ruta: /agregar_elemento_tupla/<elemento>/<tupla>
Método: GET
Descripción: Agrega un elemento a una tupla y crea una nueva tupla.
Eliminar un elemento de una tupla y crear una nueva tupla

# Ruta: /eliminar_elemento_tupla/<elemento>
Método: GET
Descripción: Elimina un elemento de una tupla y crea una nueva tupla.
Concatenar dos tuplas en una nueva tupla

# Ruta: /concatenar_tuplas
Método: GET
Descripción: Concatena dos tuplas proporcionadas en los parámetros de consulta para crear una nueva tupla.
Revertir el orden de una tupla y crear una nueva tupla

# Ruta: /revertir_tupla
Método: GET
Descripción: Revierte el orden de una tupla y crea una nueva tupla.
