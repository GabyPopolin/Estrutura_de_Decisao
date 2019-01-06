'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
e escreva o valor a ser pago pelo cliente.'''

morango = float(input('Digite a quantidade (em KG) de morangos que você está adquirindo: '))
maca = float(input('Digite a quantidade (em KG) de maçãs que você está adquirindo: '))

fruta = morango + maca

print('')
if morango > 5:
    valor_morango = morango * 2.2
    print('Você levando {}KG de morango, ele saem por R$ {:.2f}.' .format(morango, valor_morango))
else:
    valor_morango = morango * 2.5
    print('Você levando {}KG de morango, ele saem por R$ {:.2f}.' .format(morango, valor_morango))

if maca > 5:
        valor_maca = maca * 1.5
        print('Você levando {}KG de maçã, elas saem por R$ {:.2f}.' .format(maca, valor_maca))
else:
    valor_maca = maca * 1.8
    print('Você levando {}KG de maçã, elas saem por R$ {:.2f}.' .format(maca, valor_maca))

    valor_total = valor_morango + valor_maca

    print('')
    if fruta > 8 or valor_total > 25:
        desc = (valor_total * 10) / 100
        pagar = valor_total - desc
        print('Você ganhou mais um desconto de 10% (R$ {:.2f}) e irá pagar apenas R$ {:.2f} pelo o que está levando.' .format(desc, pagar))
    else:
        print('Você irá pagar R$ {:.2f} pelo o que está levando.' .format(valor_total))