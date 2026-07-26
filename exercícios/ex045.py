from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0,2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA'''
)
jogador = int(input("Qual é a sua jogada? "))

if jogador<=3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
else:
    print('JOGADA INVÁLIDA!!!')
if computador == 0:
    if jogador >= 3:
        print('Jogada INVALIDA!')
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')