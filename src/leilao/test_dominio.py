from unittest import TestCase
from src.leilao.dominio import *


class TestAvaliador(TestCase):
    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lauche_do_yuri = Lance(yuri, 100)
        lauche_do_gui = Lance(gui, 150)

        leilao = Leilao('phone')

        leilao.lance.append(lauche_do_yuri)
        leilao.lance.append(lauche_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lauche_do_yuri = Lance(yuri, 100)
        lauche_do_gui = Lance(gui, 150)

        leilao = Leilao('phone')

        leilao.lance.append(lauche_do_gui)
        leilao.lance.append(lauche_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        gui = Usuario('Gui')

        lance = Lance(gui, 150)

        leilao = Leilao('Celular')
        leilao.lance.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150, avaliador.maior_lance)
        self.assertEqual(150, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_menor_valor_quando_O_leitao_tiver_tres_lancer(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')

        lauche_do_yuri = Lance(yuri, 100)
        lauche_do_gui = Lance(gui, 150)
        lauche_do_vini = Lance(vini, 200)

        leilao = Leilao('phone')

        leilao.lance.append(lauche_do_yuri)
        leilao.lance.append(lauche_do_gui)
        leilao.lance.append(lauche_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)