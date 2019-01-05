'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

print('')
if n1 > n2 and n1 > n3:
    print('O número {}, foi o maior número informado.' .format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {}, foi o maior número informado.' .format(n2))
elif n3 > n1 and n3 > n2:
    print('O número {}, foi o maior número informado.' .format(n3))