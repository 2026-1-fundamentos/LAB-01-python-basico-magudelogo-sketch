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

import csv

def pregunta_05():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma la letra de la col 1, y el numero de la col 2
            letra = fila[0]
            numero = int(fila[1])

            # Si no esta en el diccionario, se crea
            if letra not in dic:
                dic[letra] = [numero, numero]

            # Si esta, se comprueban sus tuplas para tomar valores máximos y minimos
            else:
                if numero >= dic[letra][0]:
                    dic[letra][0] = numero

                elif numero <= dic[letra][1]:
                    dic[letra][1] = numero

    # Retorna en el orden pedido
    # En onde se mete, que se mete, ciclo for
    lista = [(clave, valor[0], valor[1]) for clave, valor in sorted(dic.items())]
    
    return lista