maiorI = 0
maiorN = ''
Mmenor = ''
media = 0
cont = 0
for c in range(1,5):
    print(f'------ {c}ª Pessoa ------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    media+=idade
    if sexo == 'M' and idade > maiorI:
        maiorI = idade
        maiorN = nome
    if sexo == 'F' and idade < 20:
        cont+=1
mt = media/4
print(f'A média de idade do grupo é de {mt} anos.')
print(f'O homem mais velho tem {maiorI} anos e se chama {maiorN}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')