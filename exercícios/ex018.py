import math 
an = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}'.format(an, seno, cosseno, tangente))