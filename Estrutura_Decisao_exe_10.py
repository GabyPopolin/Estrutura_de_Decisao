'''Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input('Em que turno você estuda? Digite: M para Matutino, V para Vespertino ou N para Noturno. '))

t = turno.upper()

print('')
if t == 'M':
    print('Bom dia, caro aluno!')
elif t == 'V':
    print('Boa tarde, caro aluno!')
elif t == 'N':
    print('Boa noite, caro aluno!')
else:
    print('O valor informado, é um valor inválido! Por favor, tente novamente.')