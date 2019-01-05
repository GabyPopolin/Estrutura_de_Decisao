'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

num = [n1 , n2 , n3]
num.sort(reverse=True)

print('')
print(num)