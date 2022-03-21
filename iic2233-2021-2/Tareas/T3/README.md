# Tarea 3:DCCalamar

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 23 pts (18%)
##### ✅ Protocolo
##### ✅ Correcto uso de sockets
##### ✅ Conexión
##### ✅ Manejo de clientes
#### Arquitectura Cliente - Servidor: 31 pts (24%)
##### ✅ Roles
##### ✅ Consistencia
##### ✅ Logs
#### Manejo de Bytes: 20 pts (15%)
##### 🟠 Codificación
##### 🟠 Decodificación
##### ✅ Encriptación
##### ✅ Integración
#### Interfaz gráfica: 31 pts (24%)
##### ✅ Modelación
##### ✅ Ventana inicio
##### ✅ Sala Principal
##### ✅ Ventana de Invitación
##### ✅ Sala de juego
##### ✅ Ventana final
#### Reglas de DCCalamar: 21 pts (16%)
##### ✅ Inicio del juego
##### ✅ Ronda
##### ✅ Termino del juego
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON)
#### Bonus: 5 décimas máximo
##### ✅ Cheatcode
##### ✅ Turnos con tiempo
## Ejecución :computer:
Un módulo principal de la tarea a ejecutar es  ```main.py``` en ```T2/clientes```. Además, se debe tener los siguientes archivos:
1. ```ventana_inicio.py``` en ```frontend```
2. ```ventana_juego.py``` en ```frontend```
3. ```ventana_principal.py``` en ```frontend```
4. ```ventana_reto.py``` en ```frontend```
5. ```parametros.json```
6. ```logica_inicio.py``` en ```backend```
7. ```logica_juego.py``` en ```backend```
8. ```logica_principal.py``` en ```backend```
9. ```logica_reto.py``` en ```backend```
10. ```ventana_juego.ui``` en ```assets``` 
11. ```ventana_final.ui``` en ```assets``` 
12. ```ventana_principal.ui``` en ```assets```
13. ```ventana_reto.ui``` en ```assets```
14. ```cliente.py```

Otro módulo principal de la tarea a ejecutar es  ```main.py``` en ```T2/servidor```. Además, se debe tener los siguientes archivos:
1. ```parametros.json```
2. ```servidor.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5```: ```QtCore, QtGui, QtWidgets, uic``` (debe instalarse)
2. ```random```: ```choice``` 
3. ```socket```: ```socket```
4. ```threading```: ```Thread```
5. ```json```: ```load```

### Librerías propias
Por otro lado, los módulos que fueron creados e importados en ```main.py``` fueron los siguientes:

1. ```ventana_inicio.py```: Contiene a las clases ```VentanaInicio```.
2. ```ventana_juego.py```: Contiene a las clases ```VentanaJuego``` y ```Player```.
3. ```ventana_principal.py```: Contiene a las clases ```VentanaPrincipal```.
4. ```ventana_reto.py```: Contiene a las clases ```VentanaReto```.
5. ```ventana_final.py```: Contiene a las clases ```VentanaFinal```.
6. ```parametros.json```: Contiene a los parámetros para este programa.
7. ```logica_inicio.py```: Contiene a las clases ```LogicaInicio```.
8. ```logica_juego.py```: Contiene a las clases ```LogicaJuego```.
9. ```logica_principal.py```: Contiene a las clases ```LogicaPrincipal```.
10. ```logica_reto.py```: Contiene a las clases ```LogicaReto```.
11. ```cliente.py```: Contiene a las clases ```Cliente```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. La fecha tiene una limitación de edad que está dada por `ano_maximo` y `ano_minimo` que en este caso son 9999 y 1000 respectivamente.
2. El nombre de usuario tiene parámetros que cumplir como lo son `max_caract` y `min_caract` que son 11 y 1 respectivamente.
3. Un jugador, después de ser retado, retar o entrar a jugar, sigue apareciendo para los jugadores en la sala principal, pero con su botón deshabilitado.
4. Cuando se termina una ronda, se mostrará el resultado de esta por 5 segundos y después comenzará automáticamente la siguiente.
5. Por la lógica de la encriptación, solo se pueden procesar mensajes con longitud mayor a 3. Por lo tanto enviar solo un diccionario o string vacío rompe el código. Por como está configurado, eso no debería pasar nunca, incluso enviado un nombre, fecha, apuesta, etc vacía.
6. La parte de codificar y decodificar casi las logro pero me ocurría un error con las funcionas `enviar2` y `recibir_mensaje2`, el cual un mensaje al recibirlo se leía su longitud como 0, por lo que el mensaje de respuesta era None en vez de ser el mensaje correcto, o a veces incluso ocurría un IndexError en la decodificación del mensaje, porque era de largo 0. Los dejé ahí para mostrar mi avance. Estaba poniéndole mucho tiempo y me estresé en esta parte, además que era un sábado así que lo dejé hasta ahí. Sin las especificaciones que pedían, sí pude codificar y decodificar con las funciones `enviar` y `recibir_mensaje`.
7. La encriptación y decriptación están en las funciones `decodificar_mensaje` y `codificar_mensaje`, respectivamente. Espero que no preste a confusión.

P.D: Aunque no eran necesario, el terminal del cliente también contiene un par de prints que muestra lo que está pasando con el cliente.
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/6784084/how-to-pass-arguments-to-functions-by-the-click-of-button-in-pyqt/42945033: Al apretar cada botón de Retar en la Sala Principal, cada uno va a entregar como argumento el nombre del jugador que hay que retar, para el cual necesite el código de este link.

2. https://stackoverflow.com/questions/46780773/pyqt-how-do-you-clear-focus-on-startup: Para poder apretar las teclas del cheatcode en la ventana juego, y que se pueda manejar, tuve que sacar el enfoque que tenía la casilla de apuesta de la manera explicada en StackOverflow.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
