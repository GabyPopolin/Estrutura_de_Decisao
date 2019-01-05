'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

n = int(input('Digite um número: '))

if n > 0:
    print('O número {}, é um número positivo.' .format(n))
else:
    print('O número {}, é um número negativo' .format(n))
