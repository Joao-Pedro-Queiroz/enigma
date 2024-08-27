import numpy as np


def one_hot_encoding(mensagem):
    dicionario = {}
    for i, letra in enumerate(mensagem):
        if letra not in dicionario:
            dicionario[letra] = len(dicionario)
    
    matriz = np.zeros((len(mensagem), len(dicionario)))
    for i, letra in enumerate(mensagem):
        matriz[i, dicionario[letra]] = 1
    
    return matriz