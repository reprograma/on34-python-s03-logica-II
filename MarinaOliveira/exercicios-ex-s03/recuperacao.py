try:
    n1 = float(input("Insira a nota do 1º Bimestre: "))
    n2 = float(input("Insira a nota do 2º Bimestre: "))
    media = (n1+n2)/2
    print("Sua média é: ", media)

    if media >= 6:
       print("Aprovada por média. Parabéns.")
    elif media >= 3:
        print("Recuperação.")
        nota_recuperacao = float(input("Insira sua nota de recuperação: "))
        if nota_recuperacao >= 7:
          print("Aprovada na recuperação")
        else:
            print("Reprovada na recuperação")
    else:
        print("Reprovada.")
except:
    print("Você precisa digitar um número entre 0 e 10")
print("Fim da análise")