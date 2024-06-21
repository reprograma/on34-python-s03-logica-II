numero = 54

chute = int(input("Tente acertar o número entre 1 e 100: "))

if chute == numero:
    print("Você acertou!")
elif chute < numero and chute > 0:
    print("O número é mais alto")
    if (numero - 2) == chute or (numero - 1) == chute:
        print("Passou perto. Errou por um ou dois números.")
elif chute > numero and chute < 101:
    print("O número é mais baixo")
    if (numero + 2) == chute or (numero + 1) == chute:
        print("Passou perto. Errou por um ou dois números.")
else:
    print("Era necessário digitar um número entre 1 e 100")

print("O número certo é", numero)