'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Digite o primeiro valor: '))
p2 = float(input('Digite o segundo valor: '))
p3 = float(input('Digite o terceiro valor: '))

print('')
if p1 < p2 and p1 < p3:
    print('Você deve comprar o produto de valor R${:.2f}.' .format(p1))
elif p2 < p1 and p2 < p3:
    print('Você deve comprar o produto de valor R${:.2f}.' .format(p2))
elif p3 < p1 and p3 < p2:
    print('Você deve comprar o produto de valor R${:.2f}.' .format(p3))