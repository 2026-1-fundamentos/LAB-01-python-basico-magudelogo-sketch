"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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
 
 
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.
 
    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
 
    """
    filas = _cargar_filas()
    valores = {}
    for fila in filas:
        letra = fila[0]
        valor = int(fila[1])
        valores.setdefault(letra, []).append(valor)
 
    resultado = []
    for letra in sorted(valores.keys()):
        resultado.append((letra, max(valores[letra]), min(valores[letra])))
    return resultado