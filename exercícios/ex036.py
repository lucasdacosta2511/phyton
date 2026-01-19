casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual é o salário? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = 30/100 * salario
print('Para pagar uma casa de R${} em {} anos a prestação será de R${}.'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')