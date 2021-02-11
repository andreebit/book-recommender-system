
# Instrucciones #
> __¡Importante!__: Antes de continuar con la instalación, es necesario tener [docker](https://www.docker.com/) instalado.
___
## Clonar el repositorio ##
Ejecutar el comando:  
`
git clone https://github.com/andreebit/book-recommender-system.git
`
___
## Inicializar ##
En la raiz del proyecto, ejecutar el comando:  
`
docker compose up -d
`
___
## Acceder al contenedor ##
Ejecutar el comando:  
`
docker exec -it ia_api_1 bash
`
___
## Entrenar el modelo ##

> En los archivos de este repositorio ya se encuentra un modelo entrenado previamente en code/trained/books.model para realizar las pruebas necesarias, pero existe la posibilidad de volver a entrenar el modelo en caso se modifique el archivo code/data/books.csv agregando o quitando datos.

Para entrenar el modelo, es necesario descargar previamente el archivo [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing) y colocarlo en la carpeta code/trained.

Con el archivo descargado, accedemos al contenedor y ejecutamos el comando:  

`
python3 utils/model_builder.py
`
___
## Probar el sistema ##
Cuando el contenedor se haya cargado correctamente, podemos empezar con las pruebas del sistema de recomendación.  

El sistema cuenta con __3__ ___endpoints___ que pueden ser consultados:

### 1.- Listado de libros ###
`
http://localhost:5000/books
`
### 2.- Detalle de libro ###
`
http://localhost:5000/books/{bookId}
`
### 3.- Listado de libros recomendados en base a un libro ###
`
http://localhost:5000/books/{bookId}/recommendations
`

> ___{bookId}___ es cualquier id de libro obtenido del endpoint de __Listado de libros__