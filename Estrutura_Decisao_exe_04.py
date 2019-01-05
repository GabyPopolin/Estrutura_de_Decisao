'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = str(input('Digite uma letra: '))

x = letra.lower()

print('')
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print('A letra digitada é uma vogal.')

else:
    print('A letra digitada é uma consoante.')