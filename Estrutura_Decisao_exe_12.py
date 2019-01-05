'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR: Salário Bruto até 900 (inclusive) - isento
                Salário Bruto até 1500 (inclusive) - desconto de 5%
                Salário Bruto até 2500 (inclusive) - desconto de 10%
                Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
                No exemplo o valor da hora é 5 e a quantidade de hora é 220.
                        Salário Bruto: (5 * 220)        : R$ 1100,00
                        (-) IR (5%)                     : R$   55,00
                        (-) INSS ( 10%)                 : R$  110,00
                        FGTS (11%)                      : R$  121,00
                        Total de descontos              : R$  165,00
                        Salário Liquido                 : R$  935,00'''

valor = float(input('Digite o valor que você recebe por hora: '))
hora = int(input('Digite a quantidade de horas que você trabalha por dia: '))
salario = valor * hora

print('')
if salario <= 900:
    ir = 0
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    desc = inss + ir
    print('Salário Bruto                 : R$ {:.2f}' .format(salario))
    print('(-) IR                        : Você está isento do Imposto de Renda! ')
    print('(-) INSS (10%)                : R$ {:.2f}' .format(inss))
    print('FGTS (11%)                    : R$ {:.2f}' .format(fgts))
    print('Total de descontos:           : R$ {:.2f}' .format(inss))
    print('Salário Líquido:              : R$ {:.2f}' .format(salario - desc))
elif salario <= 1500:
    ir = (salario * 5) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    desc = inss + ir
    print('Salário Bruto                 : R$ {:.2f}'.format(salario))
    print('(-) IR                        : R$ {:.2f}'.format(ir))
    print('(-) INSS (10%)                : R$ {:.2f}'.format(inss))
    print('FGTS (11%)                    : R$ {:.2f}'.format(fgts))
    print('Total de descontos:           : R$ {:.2f}'.format(desc))
    print('Salário Líquido:              : R$ {:.2f}'.format(salario - desc))
elif salario <= 2500:
    ir = (salario * 10) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    desc = inss + ir
    print('Salário Bruto                 : R$ {:.2f}'.format(salario))
    print('(-) IR                        : R$ {:.2f}'.format(ir))
    print('(-) INSS (10%)                : R$ {:.2f}'.format(inss))
    print('FGTS (11%)                    : R$ {:.2f}'.format(fgts))
    print('Total de descontos:           : R$ {:.2f}'.format(desc))
    print('Salário Líquido:              : R$ {:.2f}'.format(salario - desc))
elif salario > 2500:
    ir = (salario * 20) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    desc = inss + ir
    print('Salário Bruto                 : R$ {:.2f}'.format(salario))
    print('(-) IR                        : R$ {:.2f}'.format(ir))
    print('(-) INSS (10%)                : R$ {:.2f}'.format(inss))
    print('FGTS (11%)                    : R$ {:.2f}'.format(fgts))
    print('Total de descontos:           : R$ {:.2f}'.format(desc))
    print('Salário Líquido:              : R$ {:.2f}'.format(salario - desc))