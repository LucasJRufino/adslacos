#3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
#O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.

numeroFinal = 0

while True:
    numeroUser = int(input("Insira um valor a ser adicionado: "))
    if numeroUser < 0:
        break
    numeroFinal += numeroUser
    print(numeroFinal)

print("Número não válido inserido, encerrando programa...")