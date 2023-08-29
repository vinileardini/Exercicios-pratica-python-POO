#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

entrada = int(input('Insira um valor para que seja calculado seu fatorial:'))

resultado = 1
contagem = 1

while(entrada>=contagem):
    resultado *= contagem
    contagem += 1
    
if(resultado != 1):
    print(resultado)
else:
    print('fim')










    
    



