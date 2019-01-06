'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

n = float(input('Digite um número: '))
num = round(n)

print('')
if (num // 1) == num:
    print('{} é um número inteiro!' .format(num))
else:
    print('{} é um número Decimal!' .format(num))