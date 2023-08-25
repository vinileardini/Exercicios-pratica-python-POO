#Desenvolva um programa que leia 2 números e apresente as 4 operações com estes números.

entrada_1 = int(input('Insira o 1° valor:'))
entrada_2 = int(input('Insira o 2° valor:'))

soma = entrada_1+entrada_2
subtracao = entrada_1-entrada_2
divisao = entrada_1/entrada_2
multiplicacao = entrada_1*entrada_2

print(f'''A soma é: {soma}
      A subtração é: {subtracao}
      A divisão é: {divisao}
      A multiplicação é: {multiplicacao}''')
