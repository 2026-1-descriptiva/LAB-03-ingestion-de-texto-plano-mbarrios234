"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re
import pandas as pd


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    filas = []
    with open('files/input/clusters_report.txt') as archivo:
        filas = archivo.readlines()
    filas = filas[4:]
    clusters = []
    base = {
        "numero": 0,
        "cantidad": 0,
        "porcentaje": 0,
        "palabras": ""
    }

    for fila in filas:
        if re.match('^ +[0-9]+ +', fila):
            numero, cantidad, porcentaje, *palabras = fila.split()
            base["porcentaje"] = float(porcentaje.replace(',','.'))
            base["cantidad"] = int(cantidad)
            base["numero"] = int(numero)
            palabras = ' '.join(palabras[1:])
            base["palabras"] += palabras
        elif re.match('^\n', fila) or re.match('^ +$', fila):
            base["palabras"] = base["palabras"].replace('.', '')
            clusters.append(base.values())
            base = {
                "numero": 0,
                "cantidad": 0,
                "porcentaje": 0,
                "palabras": ""
            }
            
        elif re.match('^ +[a-z]', fila):
            palabras = fila.split()
            palabras = ' '.join(palabras)
            base["palabras"] += ' ' + palabras
    columnas = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df = pd.DataFrame (clusters, columns = columnas )
    return df