import numpy as np

def balance_loteria(estadistica):
    lista_contenedora = []

    for (clave, balance) in estadistica.items():
        for _ in range(balance):
            lista_contenedora.append(clave)


estadistica = {
    'gano': 1,
    'perdio': 1000
}

otra_estadistica = {
    'gano': 1,
    'salto': 2,
    'perdio': 3
}