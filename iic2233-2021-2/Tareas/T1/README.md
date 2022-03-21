# Tarea 1: DCCapitolio :knife:

## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos: 38 pts (27%)
##### ✅  Diagrama 
##### ✅ Definición de clases, atributos y métodos 
##### ✅ Relaciones entre clases
#### Simulaciones: 12 pts (8%)
##### ✅ Crear partida 
#### Acciones: 43 pts (30%)
##### ✅ Tributo
##### ✅ Objeto
##### ✅ Ambiente
##### ✅ Arena
#### Consola: 34 pts (24%)
##### ✅ Menú inicio
##### ✅ Menú principal
##### ✅ Simular Hora
##### ✅ Robustez
#### Manejo de archivos: 15 pts (11%)
##### ✅ Archivos CSV
##### ✅ parametros.py
#### Bonus: 3 décimas máximo
##### ✅ Guardar Partida 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` en ```T1```. Además, se debe tener los siguientes archivos:
1. ```tributo.py``` en ```T1```
2. ```arena.py``` en ```T1```
3. ```ambiente.py``` en ```T1```
4. ```objeto.py``` en ```T1```
5. ```parametros.py``` en ```T1```
6. ```menu.py``` en ```T1```
7. ```cargar_archivos.py``` en ```T1```
8. ```tributos.csv``` en ```T1```
9. ```ambientes.csv``` en ```T1``` 
10. ```arenas.csv``` en ```T1``` 
11. ```objetos.csv``` en ```T1``` 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:
from random import choice, random

1. ```random```: ```choice()```
2. ```random```: ```random()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ````tributo.py````: Contiene a la clase ```Tributo```.
2. ````arena.py````: Contiene a la clase ```Arena```.
3. ````objeto.py````: Contiene a la clase abstracta ```Objeto```, y las subclases `Arma`, `Consumible` y `Especial`.
4. ````ambiente.py````: Contiene a la clase abstracta```Ambiente```, y las subclases `Playa`, `Montana` y `Bosque`.
5. ```menu.py```: Contiene las funciones: de cada menú; para actualizar las muertes de los tributos; simular la hora; y elegir el personaje y la arena.
6. ```parametros.py```: Hecha para obtener los parametros al crear un usuario.
7. ```cargar_archivos.py```: Contiene funciones para obtener los datos de los archivos ```.csv```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los objetos en las mochilas de los tributos muertos desaparecen, esto es porque no se especifica en el enunciado que el asesino pueda tomar los objetos de su víctima, por lo que no lo implementé por honor al tiempo. Importante recalcar que la lista de objetos del `.csv` no se modifica, por lo que si los patrocinadores dan un cuchillo, por ejemplo, si se puede donar otra vez un cuchillo.
2. En `arena.py`, en el método de `ejecutar_evento()`, la variable `ocurrio_evento` se calcula en base si la probabilidad del evento es mayor a un número entre 0 y 1. La lógica detrás de esto, es que si la probabilidad es 1 (siempre va a ocurrir), la variable siempre va a ser mayor al número generado por `random()`. Si la probabilidad es 0.5, solo la mitad de las veces va a ser mayor, por lógica. 
3. Las variables constante en ``parametros.py`` han sido seleccionadas al azar. No tengo la menor duda que se pueden ajustar para poder mejorar la lógica y la entretención del programa.
4. Para la clase `Ambiente` se ha añadido el atributo de `dano_eventos` de tipo diccionario, para facilitar la obtención del daño que causa cada evento.
5. Además, en la clase `Ambiente` se han añadido los atributos `humedad`, `vientos`, `precipitaciones` y `nubosidad`. El fin de esto es porque para calcular el daño, cada ambiente tiene valores diferentes para estos atributos, pero tienen el mismo nombre. Además, hay ambientes que al no tener estos atributos, en la fórmula para calcular el daño esto se traduce que esa variable es 0, por lo que el valor de estos atributos para esta clase molde queda igual a 0, y cada clase hija sobre escribirá los atributos necesarios.
6. La clase `Especial` del archivo `objeto.py` hereda de `Arma` y `Consumible` para así poder entregar los beneficios suyos y de estas clases padres, como se pide en el enunciado. Como estas clases heredan de `Objeto`, `Especial` también lo hará.
7. Si se carga una partida que se había guardado, para guardarla otra vez se puede sobreescribir, o se puede guardar como una partida a parte. La partida no se guardará sola. Si no se guarda la partida o algo pasa entre medio se perderá lo avanzado.
8. Como al guardar una partida, este se pueda sobreescribir, puede ser que se borren datos de una partida anterior.

PD: Tener el Terminal ampliado para poder apreciar todo el flujo del juego.

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué un font:
1. http://www.network-science.de/ascii/: esta página le cambia el estilo al string y está implementado en el archivo main.py en las líneas 7 a 34 y hace que se vea más bonito el final del programa.
