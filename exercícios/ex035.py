print('-=' * 20)
print('Analizador de Triângulos')
print('-=' * 20)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p + s > t and p + t > s and t + s > p:
    print('Os segmentos acima PODEM formar um Triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo')
