import numpy as np
from typing import Tuple


def fazer_dict():
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?!@#%&_-+-/* "
    dict = {}

    for i in range(len(alfabeto)):
        dict[alfabeto[i]] = i

    return dict


def one_hot_encoding(mensagem):
    dicionario = fazer_dict()
    
    matriz = np.zeros((len(dicionario), len(mensagem)))
    for i, letra in enumerate(mensagem):
        matriz[dicionario[letra], i] = 1
    
    return matriz
    


def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    identidade = np.eye(N)

    P = np.random.permutation(identidade)
    R = np.random.permutation(identidade)

    return (P, R)


def encriptar_enigma(mensagem : str, P : np.ndarray, Q : np.ndarray) -> str:
    raise NotImplementedError


def decriptar_enigma(mensagem_encriptada : str, P : np.ndarray, Q : np.ndarray) -> str:
    raise NotImplementedError

print(one_hot_encoding("Joao"))