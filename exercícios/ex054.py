from datetime import date
atual = date.today().year
num = 0
maioridade = 0
menoridade = 0
for c in range(1,8):
    num+=1
    nasc = int(input(f'Em que ano a {num}ª pessoa nasceu'))
    idade = atual-nasc
    if idade >= 18:
        maioridade+=1
    else:
        menoridade+=1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos {menoridade} pessoas menores de idade')