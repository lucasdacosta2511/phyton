largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
tinta = area/2
print('sua parede tem dimensão de {} x {} e sua área é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, será necessário {}l de tinta'.format(tinta))