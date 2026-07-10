"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
import csv

def pregunta_10():
    route = "files/input/data.csv"
    lista = []
    # Diccionario que almacena los registros
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma la letra, junto con las cantidades de datos de la columna 4 y 5
            letra = fila[0]
            cantidad_col4 = len(fila[3].split(','))
            cantidad_col5 = len(fila[4].split(','))
            lista.append((letra, cantidad_col4, cantidad_col5))
    
    return lista