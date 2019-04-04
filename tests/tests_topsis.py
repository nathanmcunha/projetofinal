import unittest

import numpy as np

from topsis.topsis2 import TopSis


class MyTestCase(unittest.TestCase):

    def test_is_soma_peso_equal_um(self):
        pesos = [0.3, 0.05, 0.6, 0.05]
        soma_pesos_esperado = TopSis.is_soma_pesos_equal_um(pesos)
        self.assertEqual(soma_pesos_esperado, True)

    def test_normaliza_matriz(self):
        matriz_normalizada_esperada = np.asarray([[0.69263564, 0.46569032, 0.35805744, 0.54997194],
                                                  [0.55410852, 0.54330537, 0.50128041, 0.54997194],
                                                  [0.4617571, 0.69853547, 0.78772636, 0.62853936]])

        matriz_decisao, num_alternativas, num_criterios, size = self.mock_topsis()

        matriz_normalizada = TopSis.normaliza_matriz(matriz_decisao, num_alternativas, num_criterios, size)
        np.testing.assert_allclose(matriz_normalizada_esperada, matriz_normalizada)

        if __name__ == '__main__':
            unittest.main()

    def mock_topsis(self):
        data = np.loadtxt('file.txt', dtype=float)
        matriz_decisao = TopSis.get_matriz_decisao(data)
        size = matriz_decisao.shape
        [num_alternativas, num_criterios] = size
        return matriz_decisao, num_alternativas, num_criterios, size
