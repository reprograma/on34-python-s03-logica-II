'''Precisamos checar a nota do 1º bimestre e do 2º bimestre e fazer a média. Se a pessoa ficou de recuperação, 
é necessário checar se tirou nota suficiente para passar. A regra é: A nota mínima de aprovação é 6.
 Se a aluna tirou ao menos que 6, ela fica de recuperação, e abaixo de 3, ela está reprovada. 
 Na recuperação, a nota mínima de aprovação é 7.

Faça um programa que peça para a pessoa entrar com as duas notas de 0 a 10 e imprima se a aluna foi aprovada, 
reprovada ou está em recuperação. Se estiver em recuperação, peça para entrar com a nota da recuperação e imprima 
se foi aprovada ou reprovada.'''


nota_1bi = int(input("insira nota do primeiro bimestre: "))
nota_2bi = int(input("insira nota do segundo bimestre: "))
 
nota = ((nota_1bi + nota_2bi)/2)
print("A média do semestre é", nota, ", a aluna(o) está ")

if nota >= 6:
    print("aprovada(o)")
elif nota < 3: 
    print("reprovada(o)")
else:
    print("na recuperação(o)")