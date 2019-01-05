'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

p = str(input('Digite aqui seu gênero: F - Feminino, M - Masculino: '))

genero = p.upper()

if genero == 'F':
    print('Feminino.' .format(genero))
elif genero == 'M':
    print('Masculino.' .format(genero))
else:
    print('Sexo Inválido!!')