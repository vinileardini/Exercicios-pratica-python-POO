#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#Frutas              ||                Até 5 Kg                   ||               Acima de 5 Kg 
#Morango         ||           R$ 2,50 por Kg             ||               R$ 2,20 por Kg 
#Maçã               ||           R$ 1,80 por Kg             ||               R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

quant_morango = float(input('Insira a quantidade de morango (em kg) comprada: '))
quant_maca = float(input('Insira a quantidade (em kg) de maçãs compradas: '))

if(quant_morango < 5):
    morango = 2.5 * quant_morango
    
else:
    morango = 2.2 * quant_morango
    
if(quant_maca < 5):
    maca = 1.8 * quant_maca

else:
    maca = 1.5 * quant_maca
    
    
valor_total = morango+maca


if(valor_total > 25.0):
    
    desconto = valor_total * 0.9
    desconto = round(desconto, 2)
    print(f'O valor da compra é de R${desconto}')
    
else:
    print(f'O valor da compra é de R${valor_total}')
    
