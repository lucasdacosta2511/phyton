from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade < 18:
    saldo = 18 - idade
    ano = nascimento + 18
    print('Ainda faltam {} para seu alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    ano = nascimento + 18
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
