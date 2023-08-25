# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

entrada_numero = int(input('Insira um número de 1-7: '))

dias = ['','Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-Feira','Sábado']

if(entrada_numero>0 & entrada_numero<=7):
    entrada_dias = dias[entrada_numero]
    print(f'O dia da semana relacionado ao valor informado é {entrada_dias}')
else:
    print('Valor informado inválido')


