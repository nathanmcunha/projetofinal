from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
from numpy.core._multiarray_umath import ndarray


class TopSis:
    matriz_decisao = ndarray
    data = ndarray

    def __init__(self, file):
        self.file = file
        try:
            self.data = np.loadtxt(file, dtype=float)
        except IOError:
            print("Problemas para abrir o arquivo")
            raise IOError
            self.pesos = cls.get_pesos(self.data)
        if self.is_soma_pesos_equal_um(self.pesos):
            print('ERROR: the sum of the weights must be 1')
            raise ValueError

        self.matriz_decisao = self.get_matriz_decisao(self.data)
        self.size = self.matriz_decisao.shape
        [self.num_alternativas, self.num_criterios] = self.size

    @classmethod
    def get_pesos(cls, data):
        return data[0, :]

    @classmethod
    def is_soma_pesos_equal_um(cls, pesos):
        if np.asarray(pesos).sum() != 1.0:
            return False
        return True

    @classmethod
    def get_custo_ou_beneficio(cls):
        return cls.data[1, :].astype(int)

    @classmethod
    def get_matriz_decisao(cls, data):
        return data[2:, :]

    @classmethod
    def normaliza_matriz(cls, matriz_decisao, num_alternativas, num_criterios, size):
        normalizada = np.zeros(size, dtype=float)
        m = matriz_decisao ** 2
        m = np.sqrt(m.sum(axis=0))
        for i in range(num_alternativas):
            for j in range(num_criterios):
                normalizada[i, j] = matriz_decisao[i, j] / m[j]
        return normalizada

    @classmethod
    def introduz_pesos(cls, normalizada, pesos):
        ponderada = normalizada * pesos
        return ponderada
