import random
from time import sleep
computador = random.randint(0,5)
print('-_*_' * 15)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-_*_' * 15)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2.4)
if jogador == computador:
    print('PARABÉNS! Você consegui me vencer!')
elif jogador > 5:
    print('Número invalido')
    print('Tente novamente')

else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
