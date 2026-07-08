from colorama import Fore, Style, init
tot = 0
num = int(input('Digite um número: '))
init()
for c in range(1,num+1):
    if num % c == 0:
        print(f'{Fore.BLUE}{c}{Style.RESET_ALL}', end=' ' )
        tot+=1
    else:
        print(f'{Fore.RED}{c}{Style.RESET_ALL}' ,end=' ' )
print()
print(f'O número {num} foi divisível {tot} vezes', end=' ')
if tot == 2:
    print('e por isso ele É PRIMO')
else:
    print('e por isso ele NÃO É PRIMO')