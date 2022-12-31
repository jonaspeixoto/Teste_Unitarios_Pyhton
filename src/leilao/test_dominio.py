from unittest import TestCase
from src.leilao.dominio import *


class TestAvaliador(TestCase):
    def test_avalia(self):
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