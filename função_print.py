#sintaxe
#print(objetos, argumentos)

mensagem = "Função print()"

# #imprimindo uma variavel pré-definida
print(mensagem)

# #imprimindo uma literal string
print("Aula de Python")

# #imprimindo argumentos posicionais

# uma string e uma variável

nome = "Roberto Holanda"
print("Dev Python - ", nome)


# #duas variável

nome = "Roberto Holanda"
profissao = "Dev Python"
print(profissao, "-", nome)


# #concatenando string

nome = input("Digite seu nome: ")
print("Olá " + nome + "! Bem-vindo ao curso de Python!")

# #outra forma:

nome = input("Digite seu nome: ")
msg = "Olá " + nome + "!" + " Bem-vindo ao curso de Python!"
print(msg)

#desabilitando quebra de linha com end=""
# "Por padrão a função ptint() quebra uma linha"

print("Imprime a mensagem e muda de linha.")
print("imprime a mensagem e permanece na linha.", end="")
print(" Continuo na mesma linha!")

#print com mensagem formatada .format

nome = "Maria"
idade = 30
msg_formatada = "O nome dela é {0} e ela tem {1} anos".format(nome, idade)
print(msg_formatada)

#colocando a mensagem inteira ao inves de uutilizar a variavel msg_formatada

nome = "Maria"
idade = 30
print("O nome dela é {0} e ela tem {1} anos.".format(nome, idade))

#Usando uma f string = formated string literal 

nome = "Fábio"
peso = 73.50
msg = f"Olá, meu nome é {nome} e eu peso {peso} quilos."
print(msg)

# #outra opção : inserida diretamente no print

nome = "Roberto"
idade = 57
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

#executndo expressões diretmente dentro das f strings

a = 10
b = 5
res = f"A soma de {a} com {b} é igual a {a+b}"
print(res)

valor = 125.579637
print(f" O valor é {valor}")
print(f"O valor é {valor:.2f}")

# #usando carácteres de escape

print(f"O valor é \"{valor:.3f}\"")

nome = "João"
idade = 32
print(f"Nome:\t{nome}\tIdade:\t{idade}")
print(f"Nome: {nome}\tIdade: {idade}")
print(f"Nome: {nome}\\Idade: {idade}")
