"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

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
 
 
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    filas = _cargar_filas()
    conteo = {}
    for fila in filas:
        letra = fila[0]
        conteo[letra] = conteo.get(letra, 0) + 1
    return sorted(conteo.items())
