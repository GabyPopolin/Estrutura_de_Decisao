'''Faça um Programa que leia um número inteiro menor que '1'000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
'1'2 = '1' dezena e 2 unidades Testar com: 326, 300, '1'00, 320, 3'1'0,305, 30'1', '1'0'1', 3'1''1', '1''1''1', 25, 20, '1'0, 2'1', '1''1', '1', 7 e '1'6'''

numero = input("Digite um número menor que 1000: ")
numero_str = str(numero)
qtnumero = len(numero_str)

if qtnumero == 3:
    centena = numero_str[0:1]
    dezena = numero_str[1:2]
    unidade = numero_str[2:3]
    if centena <= '1' and dezena <= '1' and unidade <= '1':
        print('{} = {} centena, {} dezena e {} unidade.' .format(numero_str, centena, dezena, unidade))
    elif centena <= '1' and dezena <= '1' and unidade > '1':
        print('{} = {} centena, {} dezena e {} unidades.' .format(numero_str, centena, dezena, unidade))
    elif centena <='1' and dezena >'1' and unidade > '1':
        print('{} = {} centena, {} dezenas e {} unidades.' .format(numero_str, centena, dezena, unidade))
    elif centena > '1' and dezena > '1' and unidade > '1':
        print('{} = {} centenas, {} dezenas e {} unidades.' .format(numero_str, centena, dezena, unidade))
    elif centena > '1' and dezena <= '1' and unidade <= '1':
        print('{} = {} centenas, {} dezena e {} unidade.' .format(numero_str, centena, dezena, unidade))
    elif centena > '1' and dezena > '1' and unidade <= '1':
        print('{} = {} centenas, {} dezenas e {} unidade.' .format(numero_str, centena, dezena, unidade))
    elif centena > '1' and dezena <= '1' and unidade > '1':
        print('{} = {} centenas, {} dezena e {} unidades.' .format(numero_str, centena, dezena, unidade))
    elif centena <= '1' and dezena > '1' and unidade <= '1':
        print('{} = {} centena, {} dezenas e {} unidade.' .format(numero_str, centena, dezena, unidade))

if qtnumero == 2:
    dezena = numero_str[0:1]
    unidade = numero_str[1:2]
    if dezena <= '1' and unidade <= '1':
        print('{} = {} dezena e {} unidade.' .format(numero_str, dezena, unidade))
    elif dezena <= '1' and unidade > '1':
        print('{} = {} dezena e {} unidades.' .format(numero_str, dezena, unidade))
    elif dezena >'1' and unidade > '1':
        print('{} = {} dezenas e {} unidades.' .format(numero_str, dezena, unidade))
    elif dezena > '1' and unidade > '1':
        print('{} = {} dezenas e {} unidades.' .format(numero_str, dezena, unidade))
    elif dezena <= '1' and unidade <= '1':
        print('{} = {} dezena e {} unidade.' .format(numero_str, dezena, unidade))
    elif dezena > '1' and unidade <= '1':
        print('{} = {} dezenas e {} unidade.' .format(numero_str, dezena, unidade))
    elif dezena <= '1' and unidade > '1':
        print('{} = {} dezena e {} unidades.' .format(numero_str, dezena, unidade))
    elif dezena > '1' and unidade <= '1':
        print('{} = {} dezenas e {} unidade.' .format(numero_str, dezena, unidade))

if qtnumero == 1:
    unidade = numero_str[0:1]
    if unidade <= '1':
        print('{} = {} unidade.' .format(numero_str, unidade))
    elif unidade > '1':
        print('{} = {} unidades.' .format(numero_str, unidade))
    elif unidade > '1':
        print('{} = {} unidades.' .format(numero_str, unidade))
    elif unidade > '1':
        print('{} = {} unidades.' .format(numero_str, unidade))
    elif unidade <= '1':
        print('{} = {} unidade.' .format(numero_str, unidade))
    elif unidade <= '1':
        print('{} = {} unidade.' .format(numero_str, unidade))
    elif unidade > '1':
        print('{} = {} unidades.' .format(numero_str, unidade))
    elif unidade <= '1':
        print('{} = {} unidade.' .format(numero_str, unidade))