nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Pedro' or 'Maria' or 'Paulo':
    print('Seu nome é bem popular')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
