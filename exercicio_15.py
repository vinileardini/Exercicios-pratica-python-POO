#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

entrada = int(input('Insira um valor para que seja calculado seu fatorial:'))

numero_calc = 0

fatorial = []

fatorial.append(entrada)

if(entrada == 1):
    print(1)

else:
    while(entrada>1):
       calculo = entrada-1
       entrada -= 1
       fatorial.append(calculo)
       

print(f'{entrada}! = {fatorial}')



    
    



