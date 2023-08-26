#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

entrada = int(input('Insira a quantidade de repetições que deseja da sequência Fibonacci:'))

elemento_1 = 1
elemento_2 = 1


fibonacci = []

if(entrada == 1 or entrada == 2):
    fibonacci.append(elemento_1)
else:
    contagem = 3
    while(contagem <= entrada):
        sequencia = elemento_1+elemento_2
        elemento_2 = elemento_1
        elemento_1 = sequencia
        fibonacci.append(sequencia)
        contagem += 1

print(fibonacci)



    