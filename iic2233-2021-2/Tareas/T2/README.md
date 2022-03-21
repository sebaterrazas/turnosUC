# Tarea 2: DCCrossy Frog :school_satchel:

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventana de Inicio: 4 pts (3%)
##### ✅ Ventana de Inicio 
#### Ventana de Ranking: 5 pts (4%)
##### ✅ Ventana de Ranking 
#### Ventana de juego: 13 pts (11%)
##### ✅ Ventana de juego 
#### Ventana de post-nivel: 5 pts (4%)
##### ✅ Ventana post-nivel 
#### Mecánicas de juego: 69 pts (58%)
##### ✅ Personaje
##### ✅ Mapa y Áreas de juego 
##### ✅ Objetos
##### ✅ Fin de Nivel 
##### ✅ Fin del juego 
#### Cheatcodes: 8 pts (7%)
##### ✅ Pausa 
##### ✅ V + I + D
##### ✅ N + I + V
#### General: 14 pts (12%)
##### ✅ Modularización
##### ✅ Modelación
##### ✅ Archivos
##### ✅ Parametros.py
#### Bonus: 10 décimas máximo
##### ❌ Ventana de Tienda 
##### ✅ Música
##### ✅ Checkpoint 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` en ```T2```. Además, se debe tener los siguientes archivos:
1. ```ventana_inicio.py``` en ```frontend```
2. ```ventana_juego.py``` en ```frontend```
3. ```ventana_ranking.py``` en ```frontend```
4. ```ventana_post_nivel.py``` en ```frontend```
5. ```parametros.py``` en ```T1```
6. ```logica_inicio.py``` en ```backend```
7. ```logica_juego.py``` en ```backend```
8. ```logica_post_nivel.py``` en ```backend```
9. ```ventana_juego.ui``` en ```assets``` 
10. ```ventana_post_nivel.ui``` en ```assets``` 
11. ```ventana_ranking.ui``` en ```assets``` 
## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5```: ```QtCore, uic, QtGui, QtWidgets``` (debe instalarse)
2. ```random```: ```choice``` 

### Librerías propias
Por otro lado, los módulos que fueron creados e importados en ```main.py``` fueron los siguientes:

1. ```ventana_inicio.py```: Contiene a las clases ```VentanaInicio```.
2. ```ventana_juego.py```: Contiene a las clases ```VentanaJuego``` y ```Sapo```.
3. ```ventana_ranking.py```: Contiene a las clases ```VentanaRanking```.
4. ```ventana_post_nivel.py```: Contiene a las clases ```VentanaPostNivel```.
5. ```parametros.py```: Contiene a los parámetros para este programa.
6. ```logica_inicio.py```: Contiene a las clases ```LogicaInicio```.
7. ```logica_juego.py```: Contiene a las clases ```LogicaJuego``` y ```Sapo```.
8. ```logica_post_nivel.py```: Contiene a las clases ```LogicaPostNivel```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Para la música, lo más lógico era que iniciara al comienzo, y que no parara hasta el término del programa. Esto es porque no hace sentido que cada vez que se cambie de ventana, o cada vez que se ponga pausa, se reincie la música.
2. Se asume que siempre se suma puntos con la fórmula del enunciado después de terminar un nivel independiente de que si ganó o perdió en el nivel. Esto es debido a que el enunciado no especifica lo que hay que hacer en caso de derrota.
3. Como el flujo de la caminata del personaje tenía que ser fluído, tuve que manejar los inputs del teclado de forma especial. Esto se debe a que si solo utilizaba el método ```keyPressEvent``` de ```VentanaJuego``` con señales, dependía de la configuración del teclado el movimiento. Por ejemplo, mi teclado al mantener una tecla, los primeros 2 segundos lo toma como que se ha apretado 1 vez, pero si se sigue manteniendo la tecla, considera que se está apretando muchas veces esa tecla con una frecuencia alta. Esto lo arreglé agregando las teclas presionadas en un intervalo de tiempo a una lista y actualizaba los datos dependiendo del contenido de la lista. Además, de la misma forma que arreglé lo anterior, pude implementar los cheatcodes.
4. El checkpoint se ha dejado como la primera zona de pasto, por lo que si se muere después, el personaje aparece en en el chekpoint.
5. Los saltos están habilitados cuando se está encima de un tronco. O sea, para ir del pasto a un tronco se usan las teclas normales, no se salta. Para ir del último tronco al pasto sí se salta, y entre troncos también se salta. El personaje se puede mover de izquierda a derecha en un tronco, pero no va a poder salir de este, o sea no podrá avanzar a otro tronco o caerse al agua si no se salta.
6. Por como están establecidos los parámetros, en el primer nivel sí se puede saltar de un tronco a otro horizontalmente. En los niveles más avanzados el salto del sapo no es tan poderoso para poder cubrir las distancias entre los troncos que aumentan de velocidad y, por ende, de separación horizontal.

PD1: La fórmula con la que el ítem reloj suma tiempo encuentro que no tiene mucho sentido, ya que al comienzo se sumará mucho tiempo, pero cuando falta poco básicamente no se suma nada. Se pierde el propósito de agarrar un reloj cuando falta poco para salvarse.
PD2: Asegurarse de apretar las teclas de cheatcodes al mismo tiempo, porque si tienen un desfase de 0.1 segundos, mi programa los va a considerar como que fueron apretados en diferente tiempo, y el cheatcode está implementado para que las teclas estén apretadas al mismo tiempo.
## Referencias de código externo :book:

Para realizar mi tarea saqué código de la AS3. La base para la lógica del juego, como para la tarea en general, es el código pasado de la AS3 que entendía y sabía que funcionaba.

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/62667514/how-to-play-sound-with-pyqt5-qtmultimedia: Esto hace que se pueda ejecutar el archivo .wav de música en el juego.
