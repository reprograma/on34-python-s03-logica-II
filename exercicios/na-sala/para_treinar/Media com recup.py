nota1 = float(input("Entre com a 1ª nota:"))
nota2 = float(input("Entre com a 2ª nota:"))

media = (nota1 + nota2) / 2

if media >= 6 and media <= 10:
    print("Aluna aprovada")
elif media >= 3:
    print("Aluna em recuperação\n")
    nota_recup = float(input("Qual a nota da recuperação? "))
    if nota_recup >= 7:
        print("Aluna em recuperação foi aprovada")
    else:
        print("Aluna em recuperação foi reprovada")
elif media >= 0:
    print("Aluna reprovada")
else:
    print("O valor não é válido")