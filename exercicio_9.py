# Faça um Programa que leia três números e mostre o maior deles.

entrada_1 = int(input('Insira o 1° valor: '))
entrada_2 = int(input('Insira o 2° valor:'))
entrada_3 = int(input('Insira o 3° valor:'))

if entrada_1 > entrada_2:
    if entrada_1 > entrada_3:
        print(f'O maior número é {entrada_1} ')

if entrada_2 > entrada_1:
    if entrada_2 > entrada_3:
        print(f'O maior número é {entrada_2}')

if entrada_3 > entrada_1:
    if entrada_3 > entrada_2:
        print(f'O maior número é {entrada_3}')
    

if entrada_1 == entrada_2 & entrada_2 == entrada_3 & entrada_3 == entrada_1:
    print('Os valores são iguais')


