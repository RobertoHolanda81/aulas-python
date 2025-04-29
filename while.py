

num = 1

# # += operador de atribuição com incremento

while(num <= 10):
    print(num)
    num += 1 #operador de atribuiçáo com incremento
print("Laço encerrado!")

nome = None    #inicia atribuindo o valor None , 
#somente para reservar o espaço na memoria.

while True:
    print("Digite seu nome, ou x para parar")
    nome = input()
    if nome == "x" or nome == "X":
        break
    print(f"Bem-vindo, {nome}")
print("Até logo!")