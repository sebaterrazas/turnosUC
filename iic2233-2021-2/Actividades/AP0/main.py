# Debes completar esta función para que retorne la información de los ayudantes
def cargar_datos(path):
    res = []
    with open(path, 'r') as file:
        ayudantes = file.readlines()
    for a in ayudantes:
        res.append(a.rstrip().split(','))
    return res


# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(nombre_ayudante, lista_ayudantes):
    for ay in lista_ayudantes:
        if ay[0].lower() == nombre_ayudante.lower():
            return ay


# Completa esta función para que los ayudnates puedan saludar
def saludar_ayudante(info_ayudante):
    apellido = info_ayudante[0].split(' ')[-1]
    cargo = info_ayudante[1]
    return 'Hello there, General ' + str(apellido) + '.\nFelicidades, veo que eres ' + str(cargo)


if __name__ == '__main__':
    archivo = 'ayudantes.csv'
    lista_de_ayudantes = cargar_datos(archivo)
    nombre_hermano_kaii = 'Sebastián Pérez'
    lista_hmno_kaii = buscar_info_ayudante(nombre_hermano_kaii, lista_de_ayudantes)
    print(saludar_ayudante(lista_hmno_kaii))

    # El código que aquí escribas se ejecutará solo al llamar a este módulo.
    # Aquí puedes probar tu código llamando a las funciones definidas.

    # Puede llamar a cargar_datos con el path del archivo 'ayudantes.csv'
    # para probar si obtiene bien los datos.

    # Puedes intentar buscar la lista de unos de los nombres
    # que se encuentran en el archivo con la función buscar_info_ayudante.
    # Además puedes utilizar la lista obtenida para generar su saludo.

    # Hint: la función print puede se útil para revisar
    #       lo que se está retornando.
