x = y = z = False
n1 = n2 = 0

print("Digite um número: ")
n1 = int(input())
n2 = int(input("Digite outro número: "))

x = n1 == n2
print("São iguais?" , x, "\n")

z = n1 > n2
print(n1, " é maior que ", n2, "?", z, "\n")

#Note que ao não colocar "\n", não foi dado mais um espaço. 
# Pois este \n que foi concatenado após a virgula funciona como um enter. 
#\n é um carácter de escape e fica entre aspas porque é uma string.


z = n1 > n2
print(n1, " é maior que ", n2, "?", z,)

y = n1 != n2 

#Ao concatenar a varivel y que é booleana, com a string "são diferente?",
#usando o operador de concatenação (+),  precisamos converte-la para uma string.
#A função print internamente os converte para strings, porem 
#somente quando usamos a virgula para concatenar.


print("São diferentes?" + str(y))

print("São diferentes?" , y )

