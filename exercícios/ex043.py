from math import pow
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / pow(altura, 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, cuidado")
elif imc >= 30:
    print("Você está em OBESIDADE!")
elif imc >= 25:
    print("Você está em SOBREPESO")
elif imc >= 18.5:
    print("Parabéns, você está na faixa de peso NORMAL!")
else:
    print("Você está ABAIXO DO PESO normal")