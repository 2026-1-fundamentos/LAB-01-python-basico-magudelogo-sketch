"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
#RESPUESTA


import csv
import os
 
 
def _ruta_datos():
    return os.path.join(os.path.dirname(__file__), "..", "files", "data.csv")
 
 
def _cargar_filas():
    filas = []
    with open(_ruta_datos(), newline="", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter="\t")
        for fila in lector:
            if fila:
                filas.append(fila)
    return filas
 
 
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.
 
    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
 
 
    """
    filas = _cargar_filas()
    sumas = {}
    for fila in filas:
        valor = int(fila[1])
        letras = fila[3].split(",")
        for letra in letras:
            sumas[letra] = sumas.get(letra, 0) + valor
    return dict(sorted(sumas.items()))