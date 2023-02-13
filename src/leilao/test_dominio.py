from unittest import TestCase
from src.leilao.dominio import *


class TestAvaliador(TestCase):

    """ Metodo criado a cada teste e usado como padrão """
    def setUp(self):
        self.gui = Usuario('Gui')
        self.lauche_do_gui = Lance(self.gui, 150)
        self.leilao = Leilao('phone')

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        yuri = Usuario('Yuri')
        lauche_do_yuri = Lance(yuri, 100)

        self.leilao.lance.append(lauche_do_yuri)
        self.leilao.lance.append(self.lauche_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):

        yuri = Usuario('Yuri')
        lauche_do_yuri = Lance(yuri, 100)

        self.leilao.lance.append(self.lauche_do_gui)
        self.leilao.lance.append(lauche_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.lance.append(self.lauche_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150, avaliador.maior_lance)
        self.assertEqual(150, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_menor_valor_quando_O_leitao_tiver_tres_lancer(self):
        vini = Usuario('Vini')
        lauche_do_vini = Lance(vini, 200)

        yuri = Usuario('Yuri')
        lauche_do_yuri = Lance(yuri, 100)

        leilao = Leilao('phone')

        leilao.lance.append(lauche_do_yuri)
        leilao.lance.append(self.lauche_do_gui)
        leilao.lance.append(lauche_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)