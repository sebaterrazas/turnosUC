from tributo import Tributo
from arena import Arena
from objeto import Arma, Consumible, Especial
from ambiente import Bosque, Playa, Montana
from datetime import datetime


def cargar_tributos():
    with open('tributos.csv', encoding='utf-8') as f:
        lista_tributos = [t.rstrip().split(',') for t in f.readlines()[1:]]
    return [Tributo(*t) for t in lista_tributos]


def cargar_objetos():
    with open('objetos.csv', encoding='utf-8') as f:
        lista_objetos = [o.rstrip().split(',') for o in f.readlines()[1:]]
    objetos = []
    for o in lista_objetos:
        if o[1] == 'arma':
            objetos.append(Arma(*o))
        elif o[1] == 'consumible':
            objetos.append(Consumible(*o))
        elif o[1] == 'especial':
            objetos.append(Especial(*o))
    return objetos


def cargar_ambientes():
    with open('ambientes.csv', encoding='utf-8') as f:
        ambientes_raw = [a.rstrip().split(',') for a in f.readlines()[1:]]
    lista_ambientes = []
    for amb in ambientes_raw:
        ambiente_procesado = [a.split(';') for a in amb]
        eventos = {b[0]: int(b[1]) for b in ambiente_procesado[1:]}
        lista_ambientes.append([ambiente_procesado[0][0], eventos])
    ambientes = []
    for a in lista_ambientes:
        if a[0] == 'bosque':
            ambientes.append(Bosque(*a))
        elif a[0] == 'playa':
            ambientes.append(Playa(*a))
        elif a[0] == 'montaña':
            ambientes.append(Montana(*a))
    return ambientes


def cargar_arenas(jugador, tributos, ambientes):
    with open('arenas.csv', encoding='utf-8') as f:
        lista_arenas = [a.rstrip().split(',') for a in f.readlines()[1:]]
    return [Arena(*a, jugador, tributos, ambientes) for a in lista_arenas]


def guardar_partida(arena):
    with open('partidas.txt', 'r', encoding='utf-8') as file:
        partidas = [p.rstrip('\n').split('|') for p in file.readlines()]

    print('Partidas ya guardadas:')
    print('         Nombre partida          |       Fecha')
    print('---------------------------------------------------------')
    for p in partidas:
        print(f'{p[0]: ^32s} | {p[1]: ^20s}')

    elegir_nombre = True
    nombre_arena = ''
    sobreescribir_partida = ''
    while elegir_nombre:
        nombre_arena = input('\nEscribe el nombre con el que quieres guardar la partida: ')
        elegir_nombre = False
        if nombre_arena in map(lambda x: x[0], partidas):
            input_invalido = True
            while input_invalido:
                input_invalido = False
                sobreescribir_partida = input('Ya hay una partida que se llama así. '
                                              '¿Desea sobreescribirla?[y/n] ')
                if sobreescribir_partida == 'n':
                    print('Seleccione otro nombre si no desea sobreescribir el archivo.')
                    elegir_nombre = True
                if sobreescribir_partida not in ['y', 'n']:
                    input_invalido = True
                    print('Ingrese un input válido.')

    fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    datos_jugador = tributo2string(arena.jugador)
    datos_tributos = ''
    for t in arena.tributos:
        datos_tributos += tributo2string(t) + ';'
    datos_tributos = datos_tributos.rstrip(';')
    datos_ambientes = ''
    for a in arena.ambientes:
        datos_ambientes += ambiente2string(a) + ';'
    datos_ambientes = datos_ambientes.rstrip(';')

    datos_arena = str(f'{arena.nombre},{arena.dificultad},{arena.riesgo}')
    datos_arena += str(f',{datos_jugador},{datos_tributos},{datos_ambientes}')

    partida = f'{nombre_arena}|{fecha}|{datos_arena}'

    partidas_resultado = []
    for p in partidas:
        if nombre_arena == p[0]:
            partidas_resultado.append(partida)
        else:
            partidas_resultado.append('|'.join(p))
    string_partidas = '\n'.join(partidas_resultado)

    if not sobreescribir_partida:
        string_partidas += '\n' + partida

    with open('partidas.txt', 'w', encoding='utf-8') as file:
        file.write(f'{string_partidas}\n')


def tributo2string(tributo):
    nombre, distrito, edad, vida = tributo.nombre, tributo.distrito, tributo.edad, tributo.vida
    energia, agilidad, fuerza = tributo.energia, tributo.agilidad, tributo.fuerza
    ingenio, popularidad = tributo.ingenio, tributo.popularidad
    mochila = ''
    for o in tributo.mochila:
        mochila += f'{o.nombre}_{o.tipo}_{o.peso}-'
    mochila = mochila.rstrip('-')
    string_tributo = f'{nombre}:{distrito}:{edad}:{vida}:{energia}:{agilidad}'
    string_tributo += f':{fuerza}:{ingenio}:{popularidad}:{mochila}'
    return string_tributo


def ambiente2string(ambiente):
    string_ambiente = f'{ambiente.nombre}:'
    for evento, dano in ambiente.dano_eventos.items():
        string_ambiente += f'{evento}_{dano}-'
    return string_ambiente.rstrip('-')


def cargar_partida():
    with open('partidas.txt', 'r', encoding='utf-8') as file:
        partidas = [p.rstrip('\n').split('|') for p in file.readlines()]
    print('\n Nº  |         Nombre partida          |       Fecha')
    print('--------------------------------------------------------------')
    numeros_posibles = []
    for num, p in enumerate(partidas):
        numeros_posibles.append(str(num + 1))
        print(f'[{num + 1: 2d}] |{p[0]: ^32s} | {p[1]: ^20s}')
    inp = 0
    while inp not in numeros_posibles:
        inp = input('Elige una partida: ')
        if inp not in numeros_posibles:
            print('Ingrese una opción válida.')
    part = partidas[int(inp) - 1]
    print('Comenzando la partida', part[0], end='\n\n')
    list_arena = part[2].split(',')
    nom_arena = list_arena[0]
    dif_arena = list_arena[1]
    rie_arena = list_arena[2]
    lista_jugador = list_arena[3].split(':')
    lista_tributos = list_arena[4].split(';')
    lista_ambientes = list_arena[5].split(';')

    jug_arena = Tributo(*lista_jugador[:-1])
    mochila_string = lista_jugador[-1]
    objetos = []
    if mochila_string.split('-') != ['']:
        for o in mochila_string.split('-'):
            o = o.split('_')
            if o[1] == 'arma':
                objetos.append(Arma(*o))
            elif o[1] == 'consumible':
                objetos.append(Consumible(*o))
            elif o[1] == 'especial':
                objetos.append(Especial(*o))
    jug_arena.mochila = objetos

    tri_arena = []
    for t in lista_tributos:
        tributo = Tributo(*t.split(':')[:-1])
        mochila_string = t.split(':')[-1]
        objetos = []
        if mochila_string.split('-') != ['']:
            for o in mochila_string.split('-'):
                o = o.split('_')
                if o[1] == 'arma':
                    objetos.append(Arma(*o))
                elif o[1] == 'consumible':
                    objetos.append(Consumible(*o))
                elif o[1] == 'especial':
                    objetos.append(Especial(*o))
        tributo.mochila = objetos
        tri_arena.append(tributo)
    amb_arena = []
    for a in lista_ambientes:
        a_nom, a_eventos = a.split(':')
        e_dict = {}
        for e in a_eventos.split('-'):
            e_nom, e_dano = e.split('_')
            e_dict[e_nom] = int(e_dano)
        if a_nom == 'bosque':
            amb_arena.append(Bosque(a_nom, e_dict))
        elif a_nom == 'playa':
            amb_arena.append(Playa(a_nom, e_dict))
        elif a_nom == 'montaña':
            amb_arena.append(Montana(a_nom, e_dict))
    return Arena(nom_arena, dif_arena, rie_arena, jug_arena, tri_arena, amb_arena)
