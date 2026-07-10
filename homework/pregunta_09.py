"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
#RESPUEST


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
 
 
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.
 
    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}
 
    """
    filas = _cargar_filas()
    conteo = {}
    for fila in filas:
        diccionario = _parsear_diccionario(fila[4])
        for clave in diccionario:
            conteo[clave] = conteo.get(clave, 0) + 1
    return conteo