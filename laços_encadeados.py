

#Encadeamento dos laços de repetição

#Função contador externo cont_ex e função contador interno cont_in

for cont_ex in range(1,6):
    print(f"\nRodada: {cont_ex}")
    for cont_in in range(5,0,-1):
        print(f"Valor:{cont_in}")

print("Fim dos laços de repetição")

import random

for A in range(1,6):
    print(f"\nConjunto {A}")
    for B in range(5):
        num = random.randint(1,100)
        print(f"Valor: {num}")


#Para evitar que haja números duplicados
#armazena os números em um conjunto(set) em vez de apenas exibi-los,
#pois conjuntos não aceitam números duplicados.

import random

for A in range(1, 6):
    print(f'\nConjuntos{A}')
    numeros =  set()  #cria um conjunto vazio
    while len(numeros) < 5: #garante que serão gerados 5 números únicos
        num = random.randint(1, 100)
        numeros.add(num) #adiciona ao conjunto sem duplicatas.
    for num in numeros:
        print(f"Valor: {num}")
