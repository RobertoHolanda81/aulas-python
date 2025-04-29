#criando uma lista

lista = [2,6,9,4,0,12,3,7]

for item in lista:
    print(item)

#  #letras de uma palavra


palavra = "Roberto"
for letra in palavra:
    print(letra)

# #função range

# A função range cria uma lista aceitando dois argumentos, onde o primeiro
# argumento é o valor inicial e o segundo argumento é o valor final. Sendo que o
# segundo argumento é o valor limite, desta forma, esta lista só irà até o valor anterior ao valor
# do segundo argumento.

for numero in range (1,11):
    print(numero)

    for numero in range(10):
        print(numero)

nome = input("Digite seu nome: ")
for x in range(10):
    print(f"{x+1} {nome}")

# #função range(valor_inicial, valor_final, incremento ou decremento)


for x in range(2,20):
    print(x)

for x in range(2,20,2):
    print(x)

for x in range(20,1,-2):
    print(x)

#tupla é entre parenteses.

pedras = ("Rubi","Esmeralda","Quartzo","Safíra","Diamante","Turmalina")

for pedra in pedras:
    if pedra == "Quartzo":
        continue
    print(pedra)
