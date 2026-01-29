n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
m = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f},  a média do aluno é {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO.')
elif 7 > m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')