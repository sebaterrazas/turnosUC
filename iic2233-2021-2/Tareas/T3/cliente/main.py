from cliente import Cliente
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

from backend.logica_inicio import LogicaInicio
from backend.logica_principal import LogicaPrincipal, Player
from backend.logica_reto import LogicaReto
from backend.logica_juego import LogicaJuego
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_reto import VentanaReto
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal

import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


if __name__ == "__main__":
    host = p['host']
    # host = socket.gethostname()
    port = p['port']
    cliente = Cliente(host, port)

    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    # QtMultimedia.QSound.play(p.RUTA_MUSICA)

    # Instanciación de ventanas
    tamano_ventana = QRect(*p['window_size'])
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_principal = VentanaPrincipal()
    ventana_reto = VentanaReto()
    ventana_juego = VentanaJuego()
    ventana_final = VentanaFinal()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()
    logica_principal = LogicaPrincipal()
    logica_reto = LogicaReto()
    logica_juego = LogicaJuego()
    jugador = Player()

    # ~~ Conexiones de señales ~~

    # Logica Inicio
    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion
    )
    logica_inicio.senal_abrir_juego.connect(
        ventana_principal.mostrar
    )

    logica_inicio.senal_abrir_juego.connect(
        jugador.definir_nombre
    )

    logica_inicio.senal_servidor_validacion.connect(
        cliente.enviar
    )

    # Ventana Inicio
    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_usuario
    )

    # Cliente
    cliente.senal_credenciales.connect(
        logica_inicio.validar_usuario
    )

    cliente.senal_actualizar_principal.connect(
        logica_principal.actualizar
    )

    cliente.senal_reto_aceptado.connect(
        ventana_juego.mostrar
    )

    cliente.senal_reto_aceptado.connect(
        logica_juego.iniciar_juego
    )

    cliente.senal_reto_aceptado.connect(
        ventana_reto.ocultar
    )

    cliente.senal_reto_aceptado.connect(
        ventana_principal.ocultar
    )

    cliente.senal_reto_rechazado.connect(
        ventana_principal.mostrar
    )

    cliente.senal_reto_rechazado.connect(
        ventana_reto.ocultar
    )

    cliente.senal_juego_terminado.connect(
        ventana_final.mostrar
    )

    cliente.senal_juego_terminado.connect(
        ventana_juego.ocultar
    )

    cliente.senal_juego_terminado.connect(
        logica_juego.detener_tiempo
    )

    cliente.senal_apuesta_rival.connect(
        logica_juego.rival_ha_apostado
    )

    cliente.senal_cheated.connect(
        logica_juego.cheated
    )

    # Logica Principal
    logica_principal.senal_actualizar_ventana.connect(
        ventana_principal.actualizar
    )

    logica_principal.senal_retar_rival.connect(
        cliente.enviar
    )

    logica_principal.senal_retado.connect(
        ventana_principal.ocultar
    )

    logica_principal.senal_retado.connect(
        ventana_reto.mostrar
    )

    # Ventana Prinicipal

    ventana_principal.senal_retar_jugador.connect(
        logica_principal.retar_rival
    )

    # Ventana Reto
    ventana_reto.senal_respuesta_reto.connect(
        logica_reto.respuesta_reto
    )

    # Lógica Reto
    logica_reto.senal_reto_aceptado.connect(
        cliente.enviar
    )

    logica_reto.senal_reto_rechazado.connect(
        cliente.enviar
    )

    # Ventana Juego
    ventana_juego.senal_apuesta_realizada.connect(
        logica_juego.apuesta_hecha
    )

    ventana_juego.senal_tecla.connect(
        logica_juego.manejo_tecla
    )

    # Lógica Juego
    logica_juego.senal_actualizar.connect(
        ventana_juego.actualizar
    )

    logica_juego.senal_apuesta_hecha.connect(
        cliente.enviar
    )

    logica_juego.senal_fin_juego.connect(
        cliente.enviar
    )

    logica_juego.senal_fin_juego.connect(
        ventana_juego.ocultar
    )

    # Venytana Final

    ventana_final.senal_volver_inicio.connect(
        ventana_inicio.mostrar
    )

    ventana_inicio.mostrar()
    app.exec()
    # Si se cierra esta app también hay que terminar la conexión del cliente
    cliente.desconectar_usuario()

