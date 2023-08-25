# Faça um programa que pergunte se quer imprimir os pares ou impares. Na sequencia, leia 2 números e imprima todos os pares (ou ímpares) entre os 2 números.  

selecao = int(input('Deseja imprimir os pares ou os impares ? 1 - impares e 2 - pares'))

inicia_intervalo = int(input('Qual o inicio do intervalo ?'))

final_intervalo = int(input('Qual o final do intervalo ?'))

impares = []

pares = []

if(selecao == 1):

    while(inicia_intervalo<=final_intervalo):
        
        checaImpar = inicia_intervalo%2
        
        if(checaImpar != 0):
            
            impares.append(inicia_intervalo)
            
        inicia_intervalo = inicia_intervalo+1
    
    print(f'Os números ímpares são: {impares}')
    
elif(selecao == 2):
    
    while(inicia_intervalo<final_intervalo):
        
        checaPar = inicia_intervalo%2
        
        if(checaPar == 0):
            
            pares.append(inicia_intervalo)
            
    
        inicia_intervalo = inicia_intervalo+1

    print(f'Os números pares são: {pares}')
    
else:
    print('Selecione uma opção válida')