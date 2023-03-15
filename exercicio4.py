#4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
#O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
#No final, o programa deve imprimir o número total de caras e o número total de coroas.
#Use a biblioteca abaixo para números aleatórios:


import random
caras = 0
coroas = 0

vezes = int(input("Insira quantas vezes deverá lançar a moeda: "))

for i in range(vezes):
        resultado = random.randint(0, 1)
        print(resultado)
        if resultado == 0:
                caras += 1
        else:
                coroas += 1

print("Caras: ", caras)
print("Coroas: ", coroas)
