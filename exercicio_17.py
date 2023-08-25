#Na cidade futurista de Pythontown, robôs são programados para correr em uma pista especial. Você foi contratado para criar um programa que simula a corrida do robô na pista, levando em consideração sua energia e a presença de obstáculos.

#**Requisitos:**
#1. Iniciar Energia: O programa deve perguntar ao usuário a energia inicial do robô (um número inteiro entre 1 e 100).
#2. Pista: A pista é composta por 10 segmentos. Para cada segmento, o usuário deve informar se há um obstáculo (sim/não).
#3. Corrida: O robô percorrerá a pista da seguinte forma:
#   - Se houver um obstáculo, o robô gastará 3 unidades de energia para ultrapassá-lo.
#   - Se não houver um obstáculo, o robô gastará 1 unidade de energia.
#   - Se a energia do robô chegar a 0 antes de terminar a pista, ele ficará sem energia e a corrida terminará.
#4. Resultado: O programa deve exibir em qual segmento o robô parou (ou se completou a pista) e a energia restante.

#**Exemplo de Execução:**
#Energia inicial do robô: 10
#Segmento 1 - Há um obstáculo? (sim/não): não
#Segmento 2 - Há um obstáculo? (sim/não): sim
#Segmento 3 - Há um obstáculo? (sim/não): não
#...
#Segmento 10 - Há um obstáculo? (sim/não): sim
#O robô completou a pista com 2 unidades de energia restantes!
#```

#**Restrições:**- Certifique-se de que a entrada para a energia está no intervalo correto.
#- A entrada para os obstáculos deve ser 'sim' ou 'não' (sem a necessidade de considerar variações de capitalização).