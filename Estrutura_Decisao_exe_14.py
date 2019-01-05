'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou
“REPROVADO” se o conceito for D ou E.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('')
print('|   Média de Aproveitamento   |   Conceito   |')
print('|      Entre 9.0 e 10.0       |       A      |')
print('|      Entre 7.5 e  9.0       |       B      |')
print('|      Entre 6.0 e  7.5       |       C      |')
print('|      Entre 4.0 e  6.0       |       D      |')
print('|      Entre 0.0 e  4.0       |       E      |')
print('')

if media <= 4.0:
    print('Sua média foi de {}.' .format(media))
    print('Sua média equivale ao conceito "E".')
    print('Reprovado')

elif media <= 6.0:
    print('Sua média foi de {}.'.format(media))
    print('Sua média equivale ao conceito "D".')
    print('Reprovado')

elif media <= 7.5:
    print('Sua média foi de {}.'.format(media))
    print('Sua média equivale ao conceito "C".')
    print('Aprovado')

elif media <= 9.0:
    print('Sua média foi de {}.'.format(media))
    print('Sua média equivale ao conceito "B".')
    print("Aprovado")

elif media <= 10.0:
    print('Sua média foi de {}.'.format(media))
    print('Sua média equivale ao conceito "A".')
    print('Aprovado')