import unittest
import solucao as solucao
import manhattan


class TestaSolucao(unittest.TestCase):
    def test_sucessor(self):
        """
        Testa a funcao sucessor para o estado "2_3541687"
        :return:

        """
        # a lista de sucessores esperados é igual ao conjunto abaixo (ordem nao importa)
        succ_esperados = {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")}

        sucessores = solucao.sucessor("2_3541687")  # obtem os sucessores chamando a funcao implementada
        self.assertEqual(3, len(sucessores))     # verifica se foram retornados 3 sucessores
        for s in sucessores:                     # verifica se os sucessores retornados estao entre os esperados
            self.assertIn(s, succ_esperados)

    def test_expande(self):
        """
        Testa a função expande para um Node com estado "185432_67" e custo 2
        :return:
        """
        pai = solucao.Nodo("185432_67", None, "abaixo", 2)  # o pai do pai esta incorreto, mas nao interfere no teste
        # a resposta esperada deve conter nodos com os seguintes atributos (ordem dos nodos nao importa)
        resposta_esperada = {
            ("185_32467", pai, "acima", 3),
            ("1854326_7", pai, "direita", 3),
        }

        resposta = solucao.expande(pai)  # obtem a resposta chamando a funcao implementada
        self.assertEqual(2, len(resposta))  # verifica se foram retornados 2 nodos
        for nodo in resposta:
            # verifica se a tupla com os atributos do nodo esta' presente no conjunto com os nodos esperados
            self.assertIn((nodo.estado, nodo.pai, nodo.acao, nodo.custo), resposta_esperada)

    def test_bfs(self):
        """
        Testa o BFS em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.bfs("2_3541687")))
        print("Atencao! O BFS passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.bfs("185423_67"))

    def test_astar_hamming(self):
        """
        Testa o A* com dist. Hamming em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_hamming("2_3541687")))
        print("Atencao! O A* Hamming passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_hamming("185423_67"))

    def test_astar_manhattan(self):
        """
        Testa o A* com dist. Manhattan em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_manhattan("2_3541687")))
        print("Atencao! O A* Manhattan passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_manhattan("185423_67"))

    def test_dfs(self):
        """
        Testa o DFS apenas em um estado sem solucao pq ele nao e' obrigado
        a retornar o caminho minimo
        :param estado: str
        :return:
        """
        # nao ha solucao a partir do estado 185423_67
        self.assertEqual(None, solucao.dfs("185423_67"))
    
    def test_action_order(self):
        """
        Testa se BFS e A* retornam a sequencia de acoes na ordem correta
        """
        estado = "1235_6478"
        solucao_otima = ['esquerda', 'abaixo', 'direita', 'direita']
        self.assertEqual(solucao_otima, solucao.bfs(estado))
        self.assertEqual(solucao_otima, solucao.astar_hamming(estado))
        self.assertEqual(solucao_otima, solucao.astar_manhattan(estado))
        
    def test_node_init(self):
        """
        Testa inicializaçao de Nodo
        """
        estado = "1235_6478"
        pai = None
        acao = "direita"
        custo = 1
        nodo = solucao.Nodo(estado,pai,acao,custo)
        self.assertEqual(estado,nodo.estado)
        self.assertEqual(pai,nodo.pai)
        self.assertEqual(acao,nodo.acao)
        self.assertEqual(custo,nodo.custo)
        
    def test_e_estado_final(self):
        """
        Testa verificaçao de estado final
        """
        self.assertTrue(solucao.e_estado_final(solucao.Nodo("12345678_")))
        self.assertFalse(solucao.e_estado_final(solucao.Nodo("1235_6478")))
        
    def test_retorna_caminho(self):
        """
        Testa se caminho é retornado corretamente
        """
        pai = solucao.Nodo("123456_78")
        filho = solucao.Nodo("1234567_8",pai)
        neto = solucao.Nodo("12345678_",filho)
        self.assertEqual([pai,filho,neto],neto.retorna_caminho())
    def testa_calculo_manhattan(self):
        """
        Testa calculos de manhattan
        """
        nodo_uma_peca_fora_horizontal_dist_1 = solucao.Nodo("1234567_8")
        nodo_duas_peca_fora_dist_1 = solucao.Nodo("123456_78")
        nodo_uma_peca_fora_vertical_dist_1 = solucao.Nodo("12345_786")
        nodo_uma_peca_fora_vertical_e_horizontal = solucao.Nodo("_2341678_")
        nodo_duas_horizontal_uma_vertical = solucao.Nodo("12345_6__")
        nodo_baguncado = solucao.Nodo("_23145678")
        
        self.assertEqual(1,manhattan.calcula_distancia_manhattan(nodo_uma_peca_fora_horizontal_dist_1))
        self.assertEqual(2,manhattan.calcula_distancia_manhattan(nodo_duas_peca_fora_dist_1))
        self.assertEqual(1,manhattan.calcula_distancia_manhattan(nodo_uma_peca_fora_vertical_dist_1))
        self.assertEqual(2,manhattan.calcula_distancia_manhattan(nodo_uma_peca_fora_vertical_e_horizontal))
        self.assertEqual(3,manhattan.calcula_distancia_manhattan(nodo_duas_horizontal_uma_vertical))
        self.assertEqual(8,manhattan.calcula_distancia_manhattan(nodo_baguncado))
        

                    
if __name__ == '__main__':
    unittest.main()
