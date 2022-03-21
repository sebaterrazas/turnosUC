"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""

from copy import copy


class ListaReproduccion:

    def __init__(self, conjunto_videos, usuario, nombre):
        self.conjunto_videos = conjunto_videos
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        return IterarLista(copy(self.conjunto_videos))

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, conjunto_videos):
        self.conjunto_videos = conjunto_videos

    def __iter__(self):
        return self

    def __next__(self):
        if not self.conjunto_videos:
            raise StopIteration("No hay más videos para iterar")
        video_mas_afin = max(self.conjunto_videos, key=lambda x: x[1])[0]
        self.conjunto_videos = list(filter(lambda tupla_video: tupla_video[0] != video_mas_afin,
                                           self.conjunto_videos))
        return video_mas_afin
