# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo: Montar a tabuada de: 5 

valor_tabuada = int(input('Insira o valor que será utilizado na tabuada:'))

parte_um_intervalo = int(input('Insira o valor pelo qual deseja iniciar a tabuada:'))

parte_dois_intervalo = int(input('Insira o valor pelo qual deseja terminar a tabuda:'))

if(parte_dois_intervalo>=parte_um_intervalo):
    
    while(parte_um_intervalo<=parte_dois_intervalo):
        
        tabuada = valor_tabuada*parte_um_intervalo
        
        print(f'{valor_tabuada} X {parte_um_intervalo} = {tabuada}')
        
        parte_um_intervalo = parte_um_intervalo + 1
else:
    print('Informe um intervalo válido para a tabuada')
    