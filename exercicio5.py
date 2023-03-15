#5 - Faça um programa que simule a urna eletrônica.
#A tela a ser apresentada deverá ser da seguinte forma:
#As opcoes sao:
#1. Candidato Jair Rodrigues
#2. Candidato Carlos Luz
#3. Candidato Neves Rocha
#4. Nulo
#5. Branco
#Entre com o seu voto:
#O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
#informações:
#a) O número de votos de cada candidato;
#b) A porcentagem de votos nulos;
#c) A porcentagem de votos brancos;
#d) O candidato vencedor.

votos = 0
jrvotos = 0
clvotos = 0
nrvotos = 0
nulo = 0
branco = 0

while True:
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Finalizar votação")

    candidato = int(input("Escolha seu candidato: "))

    if candidato == 1:
        jrvotos += 1
    elif candidato == 2:
        clvotos += 1
    elif candidato == 3:
        nrvotos += 1
    elif candidato == 4:
        nulo += 1
    elif candidato == 5:
        branco += 1
    elif candidato == 6:
        print("------------------------")
        print("Contabilizando votos...")
        break
    else:
        print("Número inválido inserido, voto não contabilizado.")
        votos -= 1

    votos += 1

print("Votos de Jair Rodrigues: ", jrvotos)
print("Votos de Carlos Luz: ", clvotos)
print("Votos de Neves Rocha: ", nrvotos)
print("Porcentagem de votos nulos: ", nulo*100/votos, "%")
print("Porcentagem de votos em branco: ", branco*100/votos, "%")

if jrvotos > clvotos and jrvotos > nrvotos:
    print("Jair Rodrigues foi o candidato eleito.")
elif clvotos > nrvotos:
    print("Carlos Luz foi o candidato eleito.")
elif jrvotos == clvotos or clvotos == nrvotos or jrvotos == nrvotos:
    print("Houve um empate, mais um turno necessário.")
else:
    print("Neves Rocha foi o candidato eleito.")

print("------------------------")