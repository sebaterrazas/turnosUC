# Tarea 0: DCCommerce :school_satchel:

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Menú de Inicio (14pts) (14%)
##### ✅ Requisitos
##### ✅ Iniciar sesión
##### ✅ Ingresar como usuario anónimo
##### ✅ Registrar usuario
##### ✅ Salir
#### Flujo del programa (35pts) (35%) 
##### ✅ Menú Principal
##### ✅ Menú Publicaciones
##### ✅ Menú Publicaciones Realizadas
#### Entidades 15pts (15%)
##### ✅ Usuarios
##### ✅ Publicaciones
##### ✅ Comentarios
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos
#### General: 21 pts (21%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ Módulos
##### ✅ PEP8
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` en ```T0```. Además se debe crear los siguientes archivos:
1. ```clases.py``` en ```T0```
2. ```parametros.py``` en ```T0```
3. ```funciones_menu.py``` en ```T0```
4. ```usuarios.csv``` en ```T0```
5. ```comentarios.csv``` en ```T0``` 
6. ```publicaciones.csv``` en ```T0``` 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```datetime()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ````clases.py````: Contiene a ```User```, ```Post```, ```Comment```
2. ```funciones_menu.py```: Contiene las funciones de cada menú.
3. ```parametros.py```: Hecha para obtener los parametros al crear un usuario.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los usuarios no tienen contraseña, lo que se justifica porque nunca se especificó en las instrucciones, además que los usuarios predeterminados no tienen contraseña.

2. Las funcionalidades de DCCommerce están límitadas a las mencionadas en el PDF, y esto se justifica porque las instrucciones lo dicen

3. Los archivos de publicaciones.csv y comentarios.csv están ordenados por su fecha de creación, siendo las primeras líneas los más antiguos.

PD: Agrandar el terminal para poder ver de forma correcta el DCCommerce que diseñé :v:

## Referencias de código externo :book:

Para realizar mi tarea saqué un font:
1. http://www.network-science.de/ascii/: esta página le cambia el estilo al string y está implementado en el archivo main.py en las líneas 9 a 20 y hace que se vea más bonito el inicio del código

