import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtMultimedia

import parametros as p
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Sapo
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_post_nivel import VentanaPostNivel
from backend.logica_post_nivel import LogicaPostNivel


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    QtMultimedia.QSound.play(p.RUTA_MUSICA)

    # Instanciación de ventanas
    tamano_ventana = QRect(*p.WINDOW_SIZE_ARGS)
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_juego = VentanaJuego()
    ventana_ranking = VentanaRanking()
    ventana_post_nivel = VentanaPostNivel()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()
    rana_rene = Sapo(p.X_INICIAL, p.Y_INICIAL, p.WIDTH_SAPO, p.HEIGHT_SAPO, 'Q')
    logica_juego = LogicaJuego(rana_rene)
    logica_post_nivel = LogicaPostNivel()

    # ~~ Conexiones de señales ~~

    # Ventana Inicio
    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion
    )
    logica_inicio.senal_abrir_juego.connect(
        ventana_juego.mostrar_ventana
    )
    logica_inicio.senal_abrir_juego.connect(
        rana_rene.definir_nombre
    )
    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_usuario
    )

    ventana_inicio.senal_ranking.connect(
        ventana_ranking.mostrar_ventana
    )

    # Ventana Ranking
    ventana_ranking.senal_regresar.connect(
        ventana_inicio.mostrar
    )

    # Ventana Juego
    ventana_juego.senal_iniciar_juego.connect(
        logica_juego.iniciar_juego
    )

    ventana_juego.senal_iniciar_juego.connect(
        logica_juego.iniciar_juego
    )

    ventana_juego.senal_tecla.connect(
        logica_juego.manejo_tecla
    )

    ventana_juego.senal_continuar.connect(
        logica_juego.reanudar_juego
    )

    ventana_juego.senal_pausa.connect(
        logica_juego.detener_juego
    )

    logica_juego.senal_item_agarrado.connect(
        ventana_juego.consumir_item
    )

    logica_juego.senal_actualizar.connect(
        ventana_juego.actualizar
    )

    logica_juego.senal_avanzar_nivel.connect(
        ventana_post_nivel.mostrar
    )

    # Ventana Post Nivel

    ventana_post_nivel.senal_guardar_datos.connect(
        logica_post_nivel.guardar_datos
    )

    ventana_post_nivel.senal_sig_nivel.connect(
        logica_juego.sig_nivel
    )

    ventana_post_nivel.senal_sig_nivel.connect(
        ventana_juego.sig_nivel
    )

    ventana_post_nivel.senal_inicio.connect(
        ventana_inicio.mostrar
    )

    ventana_inicio.mostrar()
    app.exec()
