#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

entrada = int(input('Insira um número para verificar se é número primo:'))

multiplo = 0

for contagem in range(2,entrada):
    if(entrada % contagem == 0):
        multiplo += 1

if(multiplo == 0):
    print(f'{entrada} é primo')

else:
    print(f'{entrada} não é primo')

    
    
