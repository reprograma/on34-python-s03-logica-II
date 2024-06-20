numero = 54

chute = int(input("Tente acertar o número entre 1 e 100: "))

if chute == numero:
    print("Você acertou!")
elif chute < numero:
    print("O número é mais alto")
else:
    print("O número é mais baixo")

print("O número certo é", numero)