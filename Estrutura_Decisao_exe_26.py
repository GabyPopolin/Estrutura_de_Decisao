'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
        a) até 20 litros, desconto de 3% por litro
        b) acima de 20 litros, desconto de 5% por litro
Gasolina:
        a) até 20 litros, desconto de 4% por litro
        b) acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50
o preço do litro do álcool é R$ 1,90.'''

c = str(input('Qual foi o tipo de combustível vendido? A - Álcool , G - Gasolina: '))
l = float(input('Digite a quantidade de litros vendido: '))

print('')
if c.upper() == 'G':
    gas = 2.5 * l
    if l > 20:
        print('O valor sem o desconto é: R$ {:.2f}. Com o desconto de R$ {:.2f} (6%) em cima do valor, você terá de pagar R$ {:.2f}.' .format(
            gas, (gas * 6) / 100, gas - (gas * 6) / 100))
    else:
        print('O valor sem o desconto é: R$ {:.2f}. Com o desconto de R$ {:.2f} (4%) em cima do valor, você terá de pagar R$ {:.2f}.' .format(
            gas, (gas * 4) / 100, gas - (gas * 4) / 100))
elif c.upper() == 'A':
    alcool = 1.9 * l
    if l > 20:
        print('O valor sem o desconto é: R$ {:.2f}. Com o desconto de R$ {:.2f} (5%) em cima do valor, você terá de pagar R$ {:.2f}.' .format(
            alcool, (alcool * 5) / 100, alcool - (alcool * 5) / 100))
    else:
        print(
            'O valor sem o desconto é: R$ {:.2f}. Com o desconto de R$ {:.2f} (5%) em cima do valor, você terá de pagar R$ {:.2f}.'.format(
                alcool, (alcool * 3) / 100, alcool - (alcool * 3) / 100))
else:
    print('Esse tipo de combustível não existe.')