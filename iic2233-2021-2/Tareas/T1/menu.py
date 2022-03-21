from cargar_archivos import cargar_tributos, cargar_arenas, cargar_ambientes, guardar_partida
import parametros as p
from copy import copy


def menu_inicio():
    inp = input("""
*** Menú de Inicio ***
----------------------
[1] Iniciar partida
[2] Continuar partida
[3] Salir
""")
    valido = inp in ['1', '2', '3']
    if not valido:
        print('Ingrese un valor válido')
        return menu_inicio()
    return int(inp)


def menu_principal(arena, objetos):  # retorna True para terminar el programa, o viceversa
    personaje, rivales = arena.jugador, arena.tributos
    print("""
*** Menú Principal ***
----------------------
[1] Simulación hora
[2] Mostrar estado del tributo
[3] Utilizar objeto
[4] Resumen DCCapitolio
[5] Volver y guardar partida
[6] Salir sin guardar""")
    numeros_posibles = ['1', '2', '3', '4', '5', '6']
    inp = 0
    while inp not in numeros_posibles:
        inp = input('Elige una opción: ')
        if inp not in numeros_posibles:
            print('Ingrese una opción válida.')
    if inp == '1':
        tributos_al_comienzo = copy(arena.tributos)  # Para después ver quién murió
        dano = arena.ejecutar_evento()
        for r in rivales:
            r.vida -= dano
        personaje.vida -= dano
        actualizar_tributos(arena)

        if not (personaje.esta_vivo and arena.tributos):
            return False, False

        accion_realizada = False
        while not accion_realizada:
            accion_realizada = simular_hora(arena, objetos)

        if not (personaje.esta_vivo and arena.tributos):
            return False, False
        arena.encuentros()

        ninguno_murio = True
        string_tributos_muertos = ''
        for t in tributos_al_comienzo:
            if t not in arena.tributos:
                ninguno_murio = False
                string_tributos_muertos += f'    {t} del Distrito {t.distrito}\n'
        if ninguno_murio:
            print('Ningún tributo ha muerto')
        else:
            print('Tributos muertos (Press F to pay respects):')
            print(string_tributos_muertos)

        return False, False

    elif inp == '2':
        print(f"""
                                 Estado {personaje}
    ----------------------------------------------------------------------------
    Distrito: {personaje.distrito}
    Edad: {personaje.edad}
    Vida: {personaje.vida}
    Energía: {personaje.energia}
    Agilidad: {personaje.agilidad}
    Fuerza: {personaje.fuerza}
    Ingenio: {personaje.ingenio}
    Popularidad: {personaje.popularidad}
    Objetos: """, end='')
        if personaje.mochila:
            for o in personaje.mochila[:-1]:
                print(o.nombre, end=', ')
            print(personaje.mochila[-1].nombre)
        else:
            print()
        print('    Peso:', personaje.peso)
        return False, False
    elif inp == '3':
        if arena.jugador.mochila:
            print('\n Nº  |         Nombre objeto          |       Tipo         |     Peso')
            print('-------------------------------------------------------------------------------')
            numeros_posibles = []
            for num, o in enumerate(arena.jugador.mochila):
                numeros_posibles.append(str(num + 1))
                print(f'[{num + 1: 2d}] |{o.nombre: ^32s}|{o.tipo: ^20s}|{o.peso: ^15d}')
            inp = 0
            while inp not in numeros_posibles:
                inp = input('Elige un objeto: ')
                if inp not in numeros_posibles:
                    print('Ingrese una opción válida.')
            obj = arena.jugador.mochila[int(inp) - 1]
            print('Se ha elegido a', obj.nombre, end='\n\n')
            arena.jugador.utilizar_objeto(arena, obj)
        else:
            print(f'{personaje.nombre} no posee ningún objeto que pueda utilizar.')
        return False, False
    elif inp == '4':
        print(f"""
                               Estado DCCapitolio
    ----------------------------------------------------------------------------
    Arena: {arena.nombre}
    Dificultad: {arena.dificultad}
    Tributos vivos ({len(rivales) + 1}):
        {personaje}: {personaje.vida}""")
        for r in rivales:
            print(f'        {r}: {r.vida}')
        print(f"""    Próximo ambiente: {arena.ambientes[0].nombre}
""")
        return False, False

    elif inp == '5':
        guardar_partida(arena)
        return True, False

    elif inp == '6':
        return True, True


def eleccion_personaje():
    tributos = cargar_tributos()
    print('\n Nº  |       Nombre       |      Distrito     ')
    print('---------------------------------------------')
    numeros_posibles = []
    for num, t in enumerate(tributos):
        numeros_posibles.append(str(num + 1))
        print(f'[{num + 1:2d}] |{t.nombre: ^20s}|{t.distrito: ^20s}')
    inp = 0
    while inp not in numeros_posibles:
        inp = input('Elige un personaje: ')
        if inp not in numeros_posibles:
            print('Ingrese una opción válida.')
    personaje = tributos[int(inp) - 1]
    print('Se ha elegido a', personaje, 'del distrito', personaje.distrito)
    rivales = list(filter(lambda x: x != personaje, tributos))
    return personaje, rivales


def eleccion_arena(jugador, tributos):
    ambientes = cargar_ambientes()
    arenas = cargar_arenas(jugador, tributos, ambientes)
    print('\n Nº  |       Arena       |      Dificultad     |         Riesgo      ')
    print('---------------------------------------------------------------------')
    numeros_posibles = []
    for num, a in enumerate(arenas):
        numeros_posibles.append(str(num + 1))
        print(f'[{num + 1: 2d}] |{a.nombre: ^20s}|{a.dificultad: ^20s}|{a.riesgo: ^20.1f}')
    inp = 0
    while inp not in numeros_posibles:
        inp = input('Elige una arena: ')
        if inp not in numeros_posibles:
            print('Ingrese una opción válida.')
    arena = arenas[int(inp) - 1]
    print('Se ha elegido a', arena.nombre, end='\n\n')
    return arena


def simular_hora(arena, objetos):
    personaje = arena.jugador
    rivales = arena.tributos
    print("""
    *** Simulación de hora ***
    ----------------------
    [1] Acción heroica
    [2] Atacar a un tributo
    [3] Pedir objeto a patrocinadores
    [4] Hacerse bolita""")
    numeros_posibles = ['1', '2', '3', '4']
    inp = 0
    while inp not in numeros_posibles:
        inp = input('Elige una opción: ')
        if inp not in numeros_posibles:
            print('Ingrese una opción válida.')
    if inp == '1':
        if p.ENERGIA_ACCION_HEROICA <= personaje.energia:
            print(f'{personaje} ha realizado una acción heroica, ganando '
                  f'{p.POPULARIDAD_ACCION_HEROICA} en popularidad pero gastando '
                  f'{p.ENERGIA_ACCION_HEROICA} en energía.')
            personaje.accion_heroica()
            return True
        print(f'{personaje} no tiene energía suficiente para realizar una acción heroica.')
        return False

    elif inp == '2':
        if p.ENERGIA_ATACAR <= personaje.energia:
            print('\n Nº  |       Nombre       |      Distrito     ')
            print('---------------------------------------------')
            numeros_posibles = []
            for num, t in enumerate(rivales):
                numeros_posibles.append(str(num + 1))
                print(f'[{num + 1:2d}] |{t.nombre: ^20s}|{t.distrito: ^20s}')
            inp = 0
            while inp not in numeros_posibles:
                inp = input('Elige a quien atacar: ')
                if inp not in numeros_posibles:
                    print('Ingrese una opción válida.')
            rival = rivales[int(inp) - 1]
            dano = rival.vida
            personaje.energia -= p.ENERGIA_ATACAR
            personaje.atacar(rival)
            dano -= rival.vida
            print('Haz atacado a', rival, 'del distrito', rival.distrito,
                  'quitándole', dano, 'de vida.')
            if not rival.esta_vivo:
                print(f'¡Madre mía!, {rival} ha muerto '
                      f'ante el todopoderoso ataque de {personaje}.')
            print('Energía restante:', personaje.energia)
            return True
        print('No tienes energía para atacar, debilucho')
        return False
    elif inp == '3':
        if p.POPULARIDAD_PEDIR <= personaje.popularidad:
            obj = personaje.pedir_objeto(objetos)
            personaje.popularidad -= p.POPULARIDAD_PEDIR
            print('Canjeaste', p.POPULARIDAD_PEDIR, 'puntos en popularidad. ', end='')
            print(obj, 'ha sido añadido a tu mochila.')
            return True
        print('No eres tan cool como para hacer eso bro :]')
        return False
    elif inp == '4':
        print('Soldado que se hace bolita, sirve para otra batalla... o algo así dice el dicho')
        personaje.energia += p.ENERGIA_BOLITA
        print(f'Aumentaste tu energía hasta {personaje.energia}.')
        return True


def actualizar_tributos(arena):
    for t in arena.tributos:
        if not t.esta_vivo:
            arena.tributos.remove(t)
