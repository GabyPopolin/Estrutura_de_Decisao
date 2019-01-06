'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

print('As seguintes perguntas terão de ser respondidas apenas com "Sim" e "Não".')

print('')
perguntas = ([
'Você telefonou para a vítima? ' ,
'Você esteve no local do crime? ' ,
'Você mora perto da vítima? ' ,
'Você devia algo para a vítima? ' ,
'Já trabalhou com a vítima? '])


resposta = 0

for resp in perguntas:
    resposta += (input(resp).title() == 'Sim')


if resposta == 5:
    print('Você é o ASSASINO!!!')
elif resposta == 4 or resposta == 3:
    print('Você é o CÚMPLICE!!')
elif resposta == 2:
    print('Cuidado, você é um possível suspeito!')
else:
    print('Uffa! Dessa vez você escapou. Mas estarei de olho em você.')

