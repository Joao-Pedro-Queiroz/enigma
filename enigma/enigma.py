import numpy as np
from typing import Tuple


def one_hot_encoding(mensagem):
    


def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    identidade = np.eye(N)

    P = np.random.permutation(identidade)
    R = np.random.permutation(identidade)

    return (P, R)