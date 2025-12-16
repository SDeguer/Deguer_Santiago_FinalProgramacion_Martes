"""
Módulo para manejar el almacenamiento de gastos en formato JSON.

Este módulo guarda y lee los gastos de un archivo.
"""

import json
import os


def cargar_gastos():
    """
    Lee los gastos del archivo gastos.json.
    
    Si el archivo no existe, devuelve una lista vacía.
    """
    if os.path.exists('gastos.json'):
        archivo = open('gastos.json', 'r', encoding='utf-8')
        gastos = json.load(archivo)
        archivo.close()
        return gastos
    else:
        return []


def guardar_gastos(gastos):
    """
    Guarda los gastos en el archivo gastos.json.
    
    gastos: lista con todos los gastos
    """
    archivo = open('gastos.json', 'w', encoding='utf-8')
    json.dump(gastos, archivo, indent=4, ensure_ascii=False)
    archivo.close()