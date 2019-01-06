'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''

print('')
num = int(input('Digite um número inteiro: '))

if (num % 2) == 0:
    print('')
    print('O número {} é um número par.' .format(num))
else:
    print('')
    print('O número {} é um número ímpar.' .format(num))