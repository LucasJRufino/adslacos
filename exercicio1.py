#1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

valor = int(input("Insira um valor "))

for i in range(10):
    print(valor, " X ", (i + 1), " = ", valor * (i + 1))
