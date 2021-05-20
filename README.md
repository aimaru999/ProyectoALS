# **PROYECTO DE ALS - RECETARIUM** <br/>
<br/>

**DESCRIPCIÓN**<br/>
Foro básico para postear recetas y comentar recetas<br/>
<br/>
<br/>

**REQUISITOS PARA CORRER LA APLICACIÓN**\
-Pycharm\
-Python2.7\
-Paquete Google Application Engine\
\
\
\
**ESTRUCTURA DEL PROYECTO**\
El proyecto se estructura en 7 directorios:\
**css:** contiene los estilos CSS de la aplicación\
**handlers**: contiene los controladores GAE\
**icons**: contiene los iconos de la aplicación\
**js**: contiene archivos JavaScript usados en la validación\
**model**: contiene la definición de las entidades de la DataStore\
**resources**: contiene módulos python adicionales usadas en varios controladores\
**templates**: contiene las plantillas usadas por JINJA2\
\
\
**ENTIDADES DE LA APLICACIÓN**\
\
**Comment**: Almacena los comentarios de los usuarios:
| Atributo | Tipo de dato | Requisitos | Def |
| -- | -- | -- | -- |
| author | TextProperty | not null | Almacena el autor del comentario|
| comment| TextProperty| not null |Almacena el contenido del comentario|
| recipe_id | StringProperty | not null | Almacena la id de la receta a la que va ligado el comentario|
| title | TextProperty | not null | Almacena el título del comentario|
<br />

**Recipe**: Almacena las recetas de la aplicación:
| Atributo | Tipo de dato | Requisitos | Def |
| -- | -- | -- | -- |
| title | TextProperty | not null | Almacena el nombre de la receta|
| ingredients| TextProperty| not null |Almacena los ingredientes de la receta|
| directions | StringProperty | not null | Almacena la preparación de la receta|
| author | TextProperty | not null | Almacena el nombre del creador de la receta|
<br/>

**FUNCIONALIDADES IMPLEMENTADAS**<br/>
Por el momento la aplicación dispone de:<br/>
-Gestión de acceso a la aplicación con controlo de acceso.<br/>
-Listado de comentarios y recetas<br/>
-Añadir recetas y comentarios<br/>



