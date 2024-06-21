#Média de duas notas com recuperação
#Precisamos checar a nota do 1º bimestre e do 2º bimestre e fazer a média. 
# Se a pessoa ficou de recuperação, é necessário checar se tirou nota suficiente para passar. 
# A regra é: A nota mínima de aprovação é 6. Se a aluna tirou ao menos que 6, ela fica de recuperação, e abaixo de 3, ela está reprovada. 
# Na recuperação, a nota mínima de aprovação é 7.

#Faça um programa que peça para a pessoa entrar com as duas notas de 0 a 10 e imprima se a aluna foi aprovada, 
# reprovada ou está em recuperação. 
# Se estiver em recuperação, peça para entrar com a nota da recuperação e imprima se foi aprovada ou reprovada.

print("Bem vindo, vamos calcular a sua média, siga as instruções abaixo:")

nota1 = float(input("Digite aqui a primeira nota de 0 a 10: "))
nota2 = float(input("Digite aqui a segunda nota de 0 a 10: "))

media = (nota1+nota2) / 2

if media >= 6:
    print("PARABÉNS !!! Você foi aprovado(a) :)")

elif media >= 3:
    print("Vish... você ficou de recuperação")
    nota_recuperacao = int(input("Digite aqui a nota obtida na prova de recuperação: "))
    if nota_recuperacao >= 7:
        print("Parabéns !!! você recuperou sua nota e foi APROVADO(A) :)")
    else :
        print("Que pena, você foi reprovado... estudo mais da próxima !")

else: 
    print("Que pena, você foi Reprovado... estudo mais da próxima!")

