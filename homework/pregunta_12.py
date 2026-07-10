"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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
 
 
def _parsear_diccionario(cadena):
    diccionario = {}
    for par in cadena.split(","):
        clave, valor = par.split(":")
        diccionario[clave] = int(valor)
    return diccionario
 
 
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.
 
    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
 
    """
    filas = _cargar_filas()
    sumas = {}
    for fila in filas:
        letra = fila[0]
        diccionario = _parsear_diccionario(fila[4])
        total = sum(diccionario.values())
        sumas[letra] = sumas.get(letra, 0) + total
    return dict(sorted(sumas.items()))
