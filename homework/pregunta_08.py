"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
import csv

def pregunta_08():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma una linea de la columna 5
            num= int(fila[1])
            
            # Si no esta en el diccionario, se crea
            if num not in dic:
                dic[num] = [fila[0]]
            # Se añaden letras al diccionario en caso de que ya exista su clave
            else:
                # Se evaden los duplicados
                if fila[0] not in dic[num]:
                    dic[num].append(fila[0])
                else:
                    continue
    
    # Se ordenan las letras de cada numero correspondiente
    for clave in dic:
        dic[clave].sort()
        
    # Se ponen en formato de tupla  se ordena en base a su número(menor a mayor)
    lista = [(clave, valor) for clave, valor in sorted(dic.items())]
    
    return lista
