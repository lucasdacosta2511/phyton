real = float(input('Quanto dinhero você tem? R$'))
dolar = real / 5.54
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))