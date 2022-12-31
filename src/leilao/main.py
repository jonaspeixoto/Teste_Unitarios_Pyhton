from src.leilao.dominio import *

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lauche_do_yuri = Lance(yuri, 100)
lauche_do_gui = Lance(gui, 150)

leilao = Leilao('phone')

leilao.lance.append(lauche_do_yuri)
leilao.lance.append(lauche_do_gui)

for lance in leilao.lance:
    print(f'O usuario {lance.usuario.nome} deu o lance {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')