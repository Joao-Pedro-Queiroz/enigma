import numpy as np
from typing import Tuple


def one_hot_encoding(mensagem):
    dicionario = {}
    for i, letra in enumerate(mensagem):
        if letra not in dicionario:
            dicionario[letra] = len(dicionario)
    
    matriz = np.zeros((len(mensagem), len(dicionario)))
    for i, letra in enumerate(mensagem):
        matriz[i, dicionario[letra]] = 1
    
    return matriz
    


def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    identidade = np.eye(N)

    P = np.random.permutation(identidade)
    R = np.random.permutation(identidade)

    return (P, R)