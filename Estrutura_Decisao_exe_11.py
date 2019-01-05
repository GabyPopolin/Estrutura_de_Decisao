'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Qual é o valor do seu salário? '))

print('')
if salario <= 280:
    rea = (salario * 20) / 100
    novo = salario + rea
    print('Seu antigo salário era de R${:.2f}, e passou a ser de R${:.2f}. \nReajuste de 15% no seu salário equivale a R${:.2f}.' .format(salario, novo, rea))
elif salario <= 700:
    rea = (salario * 15) / 100
    novo = salario + rea
    print('Seu antigo salário era de R${:.2f}, e passou a ser de R${:.2f}. \nReajuste de 15% no seu salário equivale a R${:.2f}.'.format(salario, novo, rea))
elif salario <= 1500:
    rea = (salario * 10) / 100
    novo = salario + rea
    print('Seu antigo salário era de R${:.2f}, e passou a ser de R${:.2f}. \nReajuste de 15% no seu salário equivale a R${:.2f}.'.format(salario, novo, rea))
elif salario > 1500:
    rea = (salario * 5) / 100
    novo = salario + rea
    print('Seu antigo salário era de R${:.2f}, e passou a ser de R${:.2f}. \nReajuste de 15% no seu salário equivale a R${:.2f}.'.format(salario, novo, rea))