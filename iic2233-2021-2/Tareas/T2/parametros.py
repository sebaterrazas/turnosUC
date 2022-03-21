import os

# Teclas
TECLA_ARRIBA = 'w'
TECLA_DERECHA = 'd'
TECLA_IZQUIERDA = 'a'
TECLA_ABAJO = 's'
TECLA_SALTO = ' '
TECLA_PAUSA = 'p'
TECLA_D = 'd'
TECLA_I = 'i'
TECLA_V = 'v'
TECLA_N = 'n'

# Música
RUTA_MUSICA = os.path.join("frontend", "assets", "canciones",
                                       "musica.wav")

# Personaje (Sapo)
RUTA_SAPO_VERDE_QUIETO = os.path.join("frontend", "assets", "sprites",
                                       "Personajes", "Verde", "still.png")

RUTA_SAPO_VERDE_ARRIBA2 = os.path.join("frontend", "assets", "sprites",
                                       "Personajes", "Verde", "up_2.png")
RUTA_SAPO_VERDE_ARRIBA1 = os.path.join("frontend", "assets", "sprites",
                                       "Personajes", "Verde", "up_1.png")
RUTA_SAPO_VERDE_ARRIBA3 = os.path.join("frontend", "assets", "sprites",
                                       "Personajes", "Verde", "up_3.png")

RUTA_SAPO_VERDE_ABAJO2 = os.path.join("frontend", "assets", "sprites",
                                      "Personajes", "Verde", "down_2.png")
RUTA_SAPO_VERDE_ABAJO1 = os.path.join("frontend", "assets", "sprites",
                                      "Personajes", "Verde", "down_1.png")
RUTA_SAPO_VERDE_ABAJO3 = os.path.join("frontend", "assets", "sprites",
                                      "Personajes", "Verde", "down_3.png")

RUTA_SAPO_VERDE_DERECHA2 = os.path.join("frontend", "assets", "sprites",
                                        "Personajes", "Verde", "right_2.png")
RUTA_SAPO_VERDE_DERECHA1 = os.path.join("frontend", "assets", "sprites",
                                        "Personajes", "Verde", "right_1.png")
RUTA_SAPO_VERDE_DERECHA3 = os.path.join("frontend", "assets", "sprites",
                                        "Personajes", "Verde", "right_3.png")

RUTA_SAPO_VERDE_IZQUIERDA2 = os.path.join("frontend", "assets", "sprites",
                                          "Personajes", "Verde", "left_2.png")
RUTA_SAPO_VERDE_IZQUIERDA1 = os.path.join("frontend", "assets", "sprites",
                                          "Personajes", "Verde", "left_1.png")
RUTA_SAPO_VERDE_IZQUIERDA3 = os.path.join("frontend", "assets", "sprites",
                                          "Personajes", "Verde", "left_3.png")

X_INICIAL = 400
Y_INICIAL = 600
VIDAS_INICIO = 3
VELOCIDAD_CAMINAR = 40
PIXELES_SALTO_VERTICAL = 40
PIXELES_SALTO_HORIZONTAL = 70
VIDAS_TRAMPA = 3
WIDTH_SAPO = 40
HEIGHT_SAPO = 40

# Auto
RUTA_AUTO_AMARILLO_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "amarillo_right.png")
RUTA_AUTO_AMARILLO_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "amarillo_left.png")
RUTA_AUTO_AZUL_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "azul_right.png")
RUTA_AUTO_AZUL_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "azul_left.png")
RUTA_AUTO_BLANCO_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "blanco_right.png")
RUTA_AUTO_BLANCO_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "blanco_left.png")
RUTA_AUTO_MORADO_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "morado_right.png")
RUTA_AUTO_MORADO_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "morado_left.png")
RUTA_AUTO_NEGRO_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "negro_right.png")
RUTA_AUTO_NEGRO_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "negro_left.png")
RUTA_AUTO_PLATA_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "plata_right.png")
RUTA_AUTO_PLATA_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "plata_left.png")
RUTA_AUTO_ROJO_DERECHA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "rojo_right.png")
RUTA_AUTO_ROJO_IZQUIERDA = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "autos", "rojo_left.png")

RUTAS_AUTOS_DER = [
RUTA_AUTO_AMARILLO_DERECHA,
RUTA_AUTO_AZUL_DERECHA,
RUTA_AUTO_BLANCO_DERECHA,
RUTA_AUTO_MORADO_DERECHA,
RUTA_AUTO_NEGRO_DERECHA,
RUTA_AUTO_PLATA_DERECHA,
RUTA_AUTO_ROJO_DERECHA
]

RUTAS_AUTOS_IZQ = [
RUTA_AUTO_AMARILLO_IZQUIERDA,
RUTA_AUTO_AZUL_IZQUIERDA,
RUTA_AUTO_BLANCO_IZQUIERDA,
RUTA_AUTO_MORADO_IZQUIERDA,
RUTA_AUTO_NEGRO_IZQUIERDA,
RUTA_AUTO_PLATA_IZQUIERDA,
RUTA_AUTO_ROJO_IZQUIERDA
]

TIEMPO_AUTOS = 1
VELOCIDAD_AUTOS = 40
WIDTH_AUTO = 80
HEIGHT_AUTO = 40

# Troncos
RUTA_TRONCO = os.path.join("frontend", "assets", "sprites",
                                          "Mapa", "elementos", "tronco.png")
TIEMPO_TRONCOS = 2
VELOCIDAD_TRONCOS = 15
WIDTH_TRONCO = 120
HEIGHT_TRONCO = 40

# Objetos especiales
TIPOS = ['moneda', 'reloj', 'corazon', 'calavera']
RUTA_MONEDA = os.path.join("frontend", "assets", "sprites", "Objetos", "Moneda.png")
RUTA_RELOJ = os.path.join("frontend", "assets", "sprites", "Objetos", "Reloj.png")
RUTA_CORAZON = os.path.join("frontend", "assets", "sprites", "Objetos", "Corazon.png")
RUTA_CALAVERA = os.path.join("frontend", "assets", "sprites", "Objetos", "Calavera.png")
RUTA_TIPOS = {'moneda': RUTA_MONEDA, 'reloj': RUTA_RELOJ,
              'corazon': RUTA_CORAZON, 'calavera': RUTA_CALAVERA}
TIEMPO_OBJETO = 5
CANTIDAD_MONEDAS = 10
WIDTH_ITEM = 40
HEIGHT_ITEM = 40

# Ronda
DURACION_RONDA_INICIAL = 90
PONDERADOR_DIFICULTAD = 0.75

# Ventana de inicio
WINDOW_SIZE_ARGS = (100, 100, 300, 300)
MIN_CARACTERES = 3
MAX_CARACTERES = 11

stylesheet_boton = """QPushButton {
    background-color: #fd9500;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 4em;
    padding: 6px;
    color: white;
}
QPushButton:pressed {
    background-color: rgb(144, 74, 16);
    border-style: inset;
}"""


# Ventana de juego
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "assets", "ventana_juego.ui")
RUTA_ICONO = os.path.join("frontend", "assets", "sprites", "Logo.png")
RUTA_PASTO = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "pasto.png")
RUTA_RIO = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "rio.png")
RUTA_CARRETERA = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "carretera.png")
MAPAS = ['CRC', 'RCR', 'RRC', 'CCR', 'CRR', 'RCC']
DIRECCIONES = ['RLR', 'LRL']
MIN_X = 0
MAX_X = 800
MIN_Y = 120
MAX_Y = 600
Y_CHECKPOINT = 440
Y_WIN = 160
X_INICIAL_POSIBLES = {'R': 0, 'L': 840}
Y_INICIAL_POSIBLES = [[160, 200, 240], [320, 360, 400], [480, 520, 560]]
DELTA_MINIMO = 40
FPS = 5

# Ventana Ranking
RUTA_UI_VENTANA_RANKING = os.path.join("frontend", "assets", "ventana_ranking.ui")

# Ventana Post Nivel
RUTA_UI_VENTANA_POST_NIVEL = os.path.join("frontend", "assets", "ventana_post_nivel.ui")
stylesheet_nivel_superado = '''font: 13pt "Arial Rounded MT Bold";
border-radius: 5px;
color: white;
background-color: rgb(0,200,0)'''
stylesheet_nivel_no_superado = '''font: 13pt "Arial Rounded MT Bold";
border-radius: 5px;
color: white;
background-color: rgb(200,0,0)'''
