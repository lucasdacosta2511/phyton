

print('hello world')
nome = input('Qual seu nome? ')


if nome.upper() == "LUCAS":
    print("Você é meu mestre")
    senha = input('Qual é a senha? ')
    if senha == '1234':
        print('Senha correta.')
    else: 
        print('Senha incorreta.')
else: 
    print('Ola, '+ nome + ", prazer em conhece-lo, você não é meu mestre. Não te concederei acesso.")
if nome.upper() == "LUCAS":
    pai = input("Qual nome do seu pai? ") 
    if pai.lower() == "militino":
        print("Certa resposta")
    else:
        print("Resposta errada")