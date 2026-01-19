nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
elif  nome in ('Pedro', 'Maria', 'Paulo'):
    print('Seu nome é bem popular')
elif nome in 'Ana' 'Sara' 'Claudia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
