#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita".
#Se a pessoa responder positivamente entre 3 e 4 como "Cúmplice"
#Se a pessoa responder positivamente  5 como "Assassino". 
#Caso contrário, ele será classificado como "Inocente".

print('Responda somente "sim" ou "nao"')

pergunta_1 = input('Telefonou para a vítima ?').upper()
pergunta_2 = input('Esteve no local do crime ?').upper()
pergunta_3 = input('Mora perto da vítima ?').upper()
pergunta_4 = input('Devia para a vítima ?').upper()
pergunta_5 = input('Já trabalhou com a vítima ?').upper()

classificacao = 0

if(pergunta_1 == 'SIM'):
    classificacao = 1

if(pergunta_2 == 'SIM'):
    classificacao += 1
    
if(pergunta_3 == 'SIM'):
    classificacao += 1

if(pergunta_4 == 'SIM'):
    classificacao += 1

if(pergunta_5 == 'SIM'):
    classificacao += 1


    
if(classificacao == 2):
    print('Suspeita')

elif(classificacao == 3 or classificacao == 4):
    print('Cúmplice')

elif(classificacao == 5):
    print('Assassina')

else:
    print('Inocente')


