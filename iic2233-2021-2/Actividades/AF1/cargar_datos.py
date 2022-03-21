from mascota import Perro, Gato, Conejo
import os


def cargar_mascotas(archivo_mascotas):
    lista_final = []
    with open(archivo_mascotas) as file:
        for mascota in file.readlines()[1:]:
            lista_mascota = mascota.split(',')
            if lista_mascota[1] == 'gato':
                lista_final.append(Gato(lista_mascota[0], *lista_mascota[2:]))
            elif lista_mascota[1] == 'perro':
                lista_final.append(Perro(lista_mascota[0], *lista_mascota[2:]))
            elif lista_mascota[1] == 'conejo':
                lista_final.append(Gato(lista_mascota[0], *lista_mascota[2:]))
    return lista_final

