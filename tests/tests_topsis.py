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
        normalizada_com_pesos = TopSis.introduz_pesos(self.mock_matrix_normalizada_esperada(), self.mock_pesos()).round(7)
        normalizada_esperada_com_pesos = self.mock_matriz_esperada_com_pesos().round(7)
        np.testing.assert_equal(normalizada_esperada_com_pesos, normalizada_com_pesos)

    def test_get_solucoes_ideais(self):
        matriz_decisao, num_alternativas, num_criterios, size = self.mock_topsis()
        ideal_positivo_esperado = self.mock_ideal_positivo_esperado()
        ideal_negativo_esperado = self.mock_ideal_negativo_esperado()

        max = self.mock_matriz_esperada_com_pesos().max(axis=0)
        min = self.mock_matriz_esperada_com_pesos().min(axis=0)

        solucoes_ideal_pos, solucoes_ideal_neg = TopSis.get_solucoes_ideais \
            (num_criterios, max, min, self.mock_custo_ou_beneficio())

        np.testing.assert_equal(solucoes_ideal_pos.round(5), ideal_positivo_esperado.round(5))
        np.testing.assert_equal(solucoes_ideal_neg.round(5), ideal_negativo_esperado.round(5))

    def test_distancia_euclidiana(self):
        self.mock_diferenca_positiva_esperada()
        self.mock_diferenca_negativa_esperada()

        if __name__ == '__main__':
            unittest.main()

    def mock_diferenca_negativa_esperada(self):
        return np.asarray([0.25780135, 0.17686323, 0.07034498])

    def mock_diferenca_positiva_esperada(self):
        return np.asarray([0.07034498, 0.09070766, 0.25780135])

    def mock_ideal_negativo_esperado(self):
        return np.asarray([0.20779069, 0.02328452, 0.47263582, 0.0274986])

    def mock_ideal_positivo_esperado(self):
        return np.asarray([0.13852713, 0.03492677, 0.21483446, 0.03142697])

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
        return np.asarray([[0.20779069, 0.02328452, 0.21483446, 0.0274986],
                           [0.16623255, 0.02716527, 0.30076825, 0.0274986],
                           [0.13852713, 0.03492677, 0.47263582, 0.03142697]])

    def mock_pesos(self):
        return np.asarray([0.3, 0.05, 0.6, 0.05])

    def mock_custo_ou_beneficio(self):
        return np.asarray([1, 0, 1, 0]).astype(int)
