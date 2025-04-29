

n1 = n2 = 0
media = 0
faltas = 0 
 


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
faltas = int(input('Digite o número de faltas: '))

media = (n1 + n2)/2


if (faltas >= 10):
    print('Aluno reprovado por faltas')
elif (media >=7 ):
    print('Aluno Aprovado!')
    print('Parabéns)!')
elif (media >= 5):
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado')


print('Sua nota é: ' , float(media))
print('Seu número de faltas é:', int(faltas))

