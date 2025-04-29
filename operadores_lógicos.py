#AND, OR, NOT

#AND

#Condição A     Condição B      Resultado
# False          False           False
# True           False           False
# False          True            False
# True           True            True


#OR

#Condição A     Condição B      Resultado
# False          False           False
# True           False           True
# False          True            True
# True           True            True


#NOT

#Entrada    Saída
# False     True
# True      False

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = "Pode participar do evento? " + str(resultado)

print(msg)

# programa de disparo de alarme usando operador OR
# Saída False

porta =  "f"
janela = "f"

alarme = (porta == "a") or (janela == "a")
msg = "Alarme disparado? " + str(alarme)
print(msg)

 #Saída True
porta =  "a"
janela = "f"

alarme = (porta == "a") or (janela == "a")
msg = "Alarme disparado? " + str(alarme)
print(msg)

 #Saída True

porta =  "f"
janela = "a"

alarme = (porta == "a") or (janela == "a")
msg = "Alarme disparado? " + str(alarme)
print(msg)

 #Saída True

porta =  "a"
janela = "a"

alarme = (porta == "a") or (janela == "a")
msg = "Alarme disparado? " + str(alarme)
print(msg)

#Operador NOT - Inverte o valor logico

#Saída False

tem_dinheiro = False
msg = "tem dinheiro? " + str(tem_dinheiro)
print(msg)

#Saída True  "O operador NOT inverte o estado lógico"

tem_dinheiro = not tem_dinheiro
msg = "Tem dinheiro agora? " + str(tem_dinheiro)
print(msg)


