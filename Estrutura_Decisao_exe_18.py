'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))

print('')

#31 dia = 1 3 5 7 8 10 12
#30 dia = 4 6 9 11
#28 ou 29 dias = 2

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <= 31:
    print('A data informada {}/{}/{} é uma data válida.' .format(dia, mes, ano))
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia <= 30:
    print('A data informada {}/{}/{} é uma data válida.' .format(dia, mes, ano))
else:
    if mes == 2:
        if (ano % 4) == 0 and dia <= 29:
            print('O ano de {} é um ano bissexto, logo, a data informada {}/{}/{} é uma data válida.' .format(ano, dia, mes, ano))
        elif (ano % 4) != 0 and dia <= 28:
            print('O ano de {} é um ano bissexto, logo, a data informada {}/{}/{} é uma data válida.' .format(ano, dia, mes, ano))
        else:
            print('O ano de {} não é um ano bissexto, logo, a data informada {}/{}/{} é uma data inválida.' .format(ano, dia, mes, ano))