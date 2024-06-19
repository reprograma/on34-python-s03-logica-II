nota = float(input("Qual a nota? "))

if nota >= 7 and nota <= 10:
    print("Aluna aprovada")
elif nota >= 5 and nota < 7:
    print("Aluna em recuperação")
elif nota < 5 and nota >= 0:
    print("Aluna reprovada")
else:
    print("Você não digitou um valor entre 0 e 10")

'''
Atenção: temos mais condições para evitar que seja 
digitada uma nota diferente de 0 a 10