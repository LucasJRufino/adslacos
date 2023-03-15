#6 - Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança,
#esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar.
#Como saída, o programa deve imprimir na tela mês a mês o montante por 12 meses
#aplicado a uma taxa de 0,5 % ao mês de rentabilidade.

#A fórmula do montante (M) de uma aplicação financeira é dada por:

#M = P * (1 + i)^n

#onde:

#P é o capital inicial (ou principal)
#i é a taxa de juros aplicada (em forma decimal) - divida o valor dado por 100
#n é o número de períodos de tempo em que o dinheiro ficará investido.

valor = int(input("Insira o valor inicial: "))

for i in range(12):
    print("Mês ", i + 1, ": ")
    M = valor * ((1 + 0.05)**(i+1))
    print("R$%.2f" % M)
    
