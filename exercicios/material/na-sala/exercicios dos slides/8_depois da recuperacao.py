nota = float(input("Qual a nota? "))

if nota >= 7:
    print("Aluna aprovada")
elif nota >= 5:
    print("Aluna em recuperação\n")
    nota_recup = float(input("Qual a nota da recuperação? "))
    if nota_recup >= 8:
        print("Aluna em recuperação foi aprovada")
    else:
        print("Aluna em recuperação foi reprovada")
else:
    print("Aluna reprovada")