'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

print('')
if s1 > s2 + s3 and s2 > s1 + s3 and s3 > s1 + s2:
    print('Erro!!! A junção dos segmentos não forma um triângulo.')

elif s1 == s2 and s2 and s3 and s2 == s3:
    # s1 == s2 == s3:
    print('A junção dos três segmentos, sendo todos do mesmo tamanho, forma um triângulo Equilátero. ')
elif s1 == s2 or s1 == s3 or  s2 == s3:
    print('A junção dos três segmentos, sendo apenas 2 lados do mesmo tamanho, forma um triângulo Isóceles.')
elif s1 != s2 or s2 != s3 or s2 != s2:
    print('A junção dos três segmentos, sendo todos de tamanhos diferentes, formam um triângulo Escaleno.')
