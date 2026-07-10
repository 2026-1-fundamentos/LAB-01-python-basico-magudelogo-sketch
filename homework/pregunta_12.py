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

import csv
def pregunta_12():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma la clave y los valores de cada fila
            clave = fila[0]
            # Se divide cada fragmento jjj:numero
            aux = fila[4].split(',')
            # Se toma solo el numero de cada fragmento
            valores = [int(valor.split(':')[1]) for valor in aux]
            # Se suman los valores
            suma = sum(valores)

            #
            # Si no esta en el diccionario, se agrega
            if clave not in dic:
                dic[clave] = suma
            else:
                dic[clave] += suma

    return dic