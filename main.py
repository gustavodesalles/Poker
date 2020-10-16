import random
import itertools

from baralho import Baralho
from jogador import Jogador
from mesa import Mesa
from regras import Regras
from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

bars = [Card(2,"s"),Card(3,"s"),Card(4,"s"),Card(5,"s"),Card(6,"s"),Card(7,"s"),Card(8,"s"),Card(9,"s"),Card(10,"s"),Card("J","s"),Card("Q","s"),Card("K","s"),Card("A","s")]
barh = [Card(2,"h"),Card(3,"h"),Card(4,"h"),Card(5,"h"),Card(6,"h"),Card(7,"h"),Card(8,"h"),Card(9,"h"),Card(10,"h"),Card("J","h"),Card("Q","h"),Card("K","h"),Card("A","h")]
barc = [Card(2,"c"),Card(3,"c"),Card(4,"c"),Card(5,"c"),Card(6,"c"),Card(7,"c"),Card(8,"c"),Card(9,"c"),Card(10,"c"),Card("J","c"),Card("Q","c"),Card("K","c"),Card("A","c")]
bard = [Card(2,"d"),Card(3,"d"),Card(4,"d"),Card(5,"d"),Card(6,"d"),Card(7,"d"),Card(8,"d"),Card(9,"d"),Card(10,"d"),Card("J","d"),Card("Q","d"),Card("K","d"),Card("A","d")]

bar = bars + barh + barc + bard

'''def gerar_cartas():
    valor = ["ás","dois","três","quatro","cinco","seis","sete","oito","nove","dez","valete","dama","rei"]
    naipe = ["espadas","copas","ouros","paus"]
    l = []
    for n in range(4):
        for v in range(13):
            nome_carta = valor[v] + " de " + naipe[n]
            l.append(nome_carta)
    return l
'''
#bar = gerar_cartas()
j = []
for k in range(1,11):
    player = Jogador()
    j.append(player)
baralho = Baralho(bar)
mesa = Mesa()
regras = Regras()

while True:
    for i in range(0,10):
        j[i].reset()
    print("Digite o numero de jogadores entre 10 a 2 ou '0' para sair: ", end='')
    nj = int(input())
    if nj == 0:
        break
    elif nj == 1:
        print("Nao eh possivel jogar poker com 1 jogador, tente pelo menos 2")
    elif nj >= 11:
        print("Maximo de 10 jogadores por mesa")
    else:
        jogo = True
        for i in range (0, nj):
            j[i].entrarNoJogo()
        #controle de cada partida
        rodada = 0
        while jogo:
            baralho.reset(bar)
            mesa.reset()
            baralho.shuffle()
            regras.lista(j)
            baralho.darMesa(mesa)
            baralho.darJogadores(j)
            mesa.mostrarCartas()
            for i in range(0,nj):
                if j[i].bb == True:
                    print("Faça a aposta inicial: ")
                    j[i].aposta(mesa, x)
                while True:
                    print("O jogador deseja: \n 1. Aumentar a aposta; \n 2. Cobrir a aposta; \n 3. Desistir?")
                    opcao = int(input())
                    if opcao == 1:
                        j[i].aumentarAposta(mesa, x)
                    elif opcao == 2:
                        j[i].cobrirAposta(mesa)
                    elif opcao == 3:
                        j[i].desistir()
                    else:
                        print("Opção inválida")
                print("Jogador %d:" % (i+1))
                j[i].mostrarMao()
            regras.posicao(rodada)
            regras.pontuacao(j, mesa)
            mesa.distribuirDinheiro(j)
            for i in range(0,nj):
                print("Jogador %d: %d" % (i+1, j[i].dinheiro))
            rodada += 1
