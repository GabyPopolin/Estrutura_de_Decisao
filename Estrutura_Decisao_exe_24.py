'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

import os

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

print('')
print('Opções de Operações: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão')
print('')
op = int(input('Escolha a opção desejada: '))


if op == 1:
    soma = n1 + n2
    print('{} + {} = {}.' .format(n1, n2, soma))
    if (soma % 2) == 0:
        print('{} é um número PAR!' .format(soma))
    else:
        print('{} é um número ÍMPAR!' .format(soma))
    if soma >= 0:
        print('{} é um número POSITIVO!' .format(soma))
    else:
        print('{} é um número NEGATIVO!' .format(soma))
    if (soma // 1) == soma:
        print('{} é um número INTEIRO!'.format(soma))
    else:
        print('{} é um número DECIMAL!'.format(soma))

elif op == 2:
    sub = n1 - n2
    print('{} - {} = {}.' .format(n1, n2, sub))
    if (sub % 2) == 0:
        print('{} é um número PAR!' .format(sub))
    else:
        print('{} é um número ÍMPAR!' .format(sub))
    if sub >= 0:
        print('{} é um número POSITIVO!' .format(sub))
    else:
        print('{} é um número NEGATIVO!' .format(sub))
    if (sub // 1) == sub:
        print('{} é um número INTEIRO!'.format(sub))
    else:
        print('{} é um número DECIMAL!'.format(sub))

elif op == 3:
    mult = n1 * n2
    print('{} x {} = {}.' .format(n1, n2, mult))
    if (mult % 2) == 0:
        print('{} é um número PAR!' .format(mult))
    else:
        print('{} é um número ÍMPAR!' .format(mult))
    if mult >= 0:
        print('{} é um número POSITIVO!' .format(mult))
    else:
        print('{} é um número NEGATIVO!' .format(mult))
    if (mult // 1) == mult:
        print('{} é um número INTEIRO!'.format(mult))
    else:
        print('{} é um número DECIMAL!'.format(mult))

elif op == 4:
    div = n1 / n2
    print('{} / {} = {}.' .format(n1, n2, div))
    if (div % 2) == 0:
        print('{} é um número PAR!' .format(div))
    else:
        print('{} é um número ÍMPAR!' .format(div))
    if div >= 0:
        print('{} é um número POSITIVO!' .format(div))
    else:
        print('{} é um número NEGATIVO!' .format(div))
    if (div // 1) == div:
        print('{} é um número INTEIRO!'.format(div))
    else:
        print('{} é um número DECIMAL!'.format(div))

else:
    print('Erro!!! Número de opção escolhida não existe. Por favor, tente novamente com uma operação que exista.')