'''Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))

media = (n1 + n2 + n3 + n4) / 4

print('')
print('A média final do aluno foi {:.2f}' .format(media))
if media == 10:
    print('O aluno está Aprovado com Distinção.')
elif media == 9.9 or media >= 7:
    print('O aluno está Aprovado.')
elif media <= 6.9:
    print('O aluno está Reprovado.')
