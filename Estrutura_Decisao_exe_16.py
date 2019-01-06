'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não
deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
from math import sqrt

print('')
print(' ax² + bx + c = 0')
a = int(input('Digite um valor que irá ocupar o lugar da letra "a": '))
if a == 0:
    print('')
    print('Número informado: {}. Uma equação de segundo grau não pode ser iniciada com 0.'.format(a))
else:
    b = int(input('Digite um valor que irá ocupar o lugar da letra "b": '))
    c = int(input('Digite um valor que irá ocupar o lugar da letra "c": '))

    print('')
    print('A equação ficou da seguinte forma: \n {}x² + {}x + {} = 0' .format(a, b, c))

    print('')
    print('Fórmula da Bhaskara: x = -b ± √b² - 4ac / 2a')
    print('A Bhaskara ficará assim: x = -{} ± √{}² - 4.{}.{} / 2.{}' .format(b, b, a, c, a))

    print('')
    print('A fórmula de Bhaskara é apresenta de duas formas: \n x1 = -b + √b² - 4ac / 2a')
    print(' x2 = -b - √b² - 4ac / 2a')

    print('')
    print('Fórmula de Bhaskara com os valores definidos:')
    print(' x1 = -{} + √{}² - 4.{}.{} / 2.{}' .format(b, b, a, c, a), '\n x2 = -{} . √{}² - 4.{}.{} / 2.{}' .format(b, b, a, c, a))

    result = (b ** 2) - (4 * a * c)

    print('')
    if result > 0:
        x1 = (-(b) + (sqrt(result))) / (2 * a)
        x2 = (-(b) - (sqrt(result))) / (2 * a)
        print('O resultado da primeira operação é: {:.2f}.' .format(x1))
        print('O resultado da segunda operação é: {:.2f}.' .format(x2))

        r1 = x1 ** 2 - 5 * x1 + 6
        r2 = x2 ** 2 - 5 * x2 + 6

        if x1 < 0:
            print("A equação não possui raízes reais.")
        elif x1 == 0:
            print('A equação possui apenas uma raiz real')
        elif x1 > 0 and x2 > 0:
            print('A equação possui duas raízes reais.')