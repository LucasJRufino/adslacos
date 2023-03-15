#7 - Faça um programa que mostre o fatorial de um número fornecido pelo usuário.

numero = int(input("Insira o valor: "))
final = 1

for i in range(1, numero+1):
    final = final * i
print(final)