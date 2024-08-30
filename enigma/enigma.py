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
    Q = np.random.permutation(identidade)

    return (P, Q)


def encriptar_enigma(mensagem : str, P : np.ndarray, Q : np.ndarray) -> str:
    dicionario = fazer_dict()
    matriz_mensagem = one_hot_encoding(mensagem)
    matriz_permutacao = P @ Q
    matriz_permutada = matriz_permutacao @ matriz_mensagem
    mensagem_codificada = ''
    contador = 0

    while len(mensagem_codificada) < len(mensagem):
        for l in range(len(matriz_permutada)):
            if matriz_permutada[l][contador] == 1:
                for caractere in dicionario.keys():
                    if dicionario[caractere] == l:
                        mensagem_codificada += caractere
                        contador += 1
                        break
        
                break

    return mensagem_codificada



def decriptar_enigma(mensagem_encriptada : str, P : np.ndarray, Q : np.ndarray) -> str:
    dicionario = fazer_dict()
    matriz_mensagem_codificada = one_hot_encoding(mensagem_encriptada)
    matriz_permutacao = P @ Q
    matriz_permutada = np.linalg.inv(matriz_permutacao) @ matriz_mensagem_codificada
    mensagem_descodificada = ''
    contador = 0

    while len(mensagem_descodificada) < len(mensagem_encriptada):
        for l in range(len(matriz_permutada)):
            if matriz_permutada[l][contador] == 1:
                for caractere in dicionario.keys():
                    if dicionario[caractere] == l:
                        mensagem_descodificada += caractere
                        contador += 1
                        break
        
                break

    return mensagem_descodificada