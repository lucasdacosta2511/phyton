p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p < s + t and s< p + t and t < p + s:
    print('Os segmrntos acima PODEM FORMAR um triangulo ',end='')
    if p == s == t:
        print('EQUILATERO!')
    elif p == s or p == t or s == t:
        print('ISÓCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
