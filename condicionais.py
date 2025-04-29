
#if, elif, else

#simple, composto, encadeado ou aninhado

#Simples
 
n1 = n2 = 0
media = 0

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda  nota: "))

#Calcular a média aritmética das notas

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")


print("Sua média é: {}".format(media))

#composto

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
else:
    print("Aluno Reprovado!")
print("Sua média é: {}".format(media))

#encadeado ou aninhado

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif(media >= 5):
    print("Você está de recuperação")
else:
    print("Aluno Reprovado!")

print("Sua média é: {}".format(media))

#Alternativas ao format():

#nesta primeira opcão, conversão explicita 
# para string com "str(media)", porque
#a concatenação com outra string foi feita com (+).

print("Sua média é: " + str(media))

#Já no segundo a conversão implicita com f-string 
# torna o codigo mais limpo e legivel.


print(f"Sua média é: {media}")

#nesta outra alternativa a concatenação com virgula
#tambem funciona pois o print()aceita multiplos argumentos
# separados por virgula.
#É direto e funcional.

print('Sua média é: ', media)


#Exercício

faltas = 0
n1 = n2 = 0



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
faltas = int(input("Entre com a quantidade de faltas: "))

media = (n1 + n2)/2


if (faltas >= 10):
    print("Aluno reprovado por faltas")
elif (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif(media >= 5):
    print("Você está de recuperação")
else:
    print("Aluno Reprovado!")

print("Sua média é: {}".format(media))
print("Seu númerto de faltas é: {}".format(faltas))


