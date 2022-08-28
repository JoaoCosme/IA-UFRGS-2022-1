import os
import unittest
import alegrete
import numpy as np


class TestAlegrete(unittest.TestCase):
    
    def test_compute_mse(self):
        try:
            data = np.genfromtxt('Trab-3/alegrete.csv', delimiter=',')
        except FileNotFoundError:
            data = np.genfromtxt('alegrete.csv', delimiter=',')
        mse = alegrete.compute_mse(0, 0, data)
        self.assertAlmostEqual(66.78348986604624, mse, 8)  # comparacao de floats com 9 casas de precisao

    def test_step_gradient(self):
        # dataset do Quiz de Otimizacao Continua
        data = np.array([
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 2]
        ])

        new_theta0, new_theta1 = alegrete.step_gradient(1, 1, data, alpha=0.1)
        # comparacao de floats com precisao de 11 casas
        self.assertAlmostEqual(0.95, new_theta0, 11)
        self.assertAlmostEqual(0.55, new_theta1, 11)
    def test_normalizacao(self):
        data = np.array([
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 2]
        ])
        
        data_normalizada = alegrete.normaliza_features(data)
        
        self.assertAlmostEqual(0.333333,data_normalizada[1][0],3)


if __name__ == '__main__':
    unittest.main()