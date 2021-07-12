import numpy as np

def balance_loteria(otros_balances):
    lista_contenedora = []

    for (name, balance) in otros_balances.items():
        for _ in range(balance):
            lista_contenedora.append(name)
    
    return lista_contenedora


balances = {
    'gano': 1,
    'perdio': 10
}
print(balance_loteria(balances))

otros_balances = {
    'gano': 1,
    'salto': 2,
    'perdio': 3
}

print(balance_loteria(otros_balances))