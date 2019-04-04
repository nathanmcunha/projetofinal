import unittest

import numpy as np

from topsis.topsis2 import TopSis


class MyTestCase(unittest.TestCase):

    def test_is_soma_peso_equal_um(self):
        pesos = [0.3, 0.05, 0.6, 0.05]
        soma_pesos_esperado = TopSis.is_soma_pesos_equal_um(pesos)
        self.assertEqual(soma_pesos_esperado, True)

    def test_normaliza_matriz(self):
        matriz_decisao, num_alternativas, num_criterios, size = self.mock_topsis()

        matriz_normalizada = TopSis.normaliza_matriz(matriz_decisao, num_alternativas, num_criterios, size)

        np.testing.assert_allclose(self.mock_matrix_normalizada_esperada(), matriz_normalizada)

    def test_introduz_pesos(self):
        mock_pesos = np.asarray([0.3, 0.05, 0.6, 0.05])
        normalizada_com_pesos = TopSis.introduz_pesos(self.mock_matrix_normalizada_esperada(), mock_pesos)
        np.testing.assert_allclose(normalizada_com_pesos, self.mock_matriz_esperada_com_pesos(), atol=1)

        if __name__ == '__main__':
            unittest.main()

    def mock_topsis(self):
        data = np.loadtxt('file.txt', dtype=float)
        matriz_decisao = TopSis.get_matriz_decisao(data)
        size = matriz_decisao.shape
        [num_alternativas, num_criterios] = size
        return matriz_decisao, num_alternativas, num_criterios, size

    def mock_matrix_normalizada_esperada(self):
        return np.asarray([[0.69263564, 0.46569032, 0.35805744, 0.54997194],
                           [0.55410852, 0.54330537, 0.50128041, 0.54997194],
                           [0.4617571, 0.69853547, 0.78772636, 0.62853936]])

    def mock_matriz_esperada_com_pesos(self):
        return [[0.20779069, 0.02328452, 0.21483446, 0.0274986],
                [0.16623255, 0.02716527, 0.30076825, 0.0274986],
                [0.13852713, 0.03492677, 0.47263582, 0.03142697]]
