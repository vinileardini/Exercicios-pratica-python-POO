# Desenvolva um programa que leia um número e diga se ele é PAR ou IMPAR. Este programa deve rodar até que um caractere não numérico seja digitado

checagem_numb = 0

while(checagem_numb == int()):
     
     entrada = int(input('Insira o número a ser verificado:'))
     
     checagem = entrada%2
     
     if(checagem == 0):
         print(f'O número {entrada} é par')
         
     else:
        print(f'O número {entrada} é ímpar')
            
        checagem_numb = entrada

print('O programa foi encerrado devido ao fato de não ter sido inserido um valor válido')