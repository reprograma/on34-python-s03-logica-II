'''nesta opção, limitamos a entrada à faixa de números maiores 
que zero e menores que 101, isto é, entre 1 e 100.
Também usamos try e except para evitar que a entrada seja
diferente de números inteiros, senão o programa quebra
'''
numero = 54

try:
    chute = int(input("Tente acertar o número entre 1 e 100: "))

    if chute == numero:
        print("Você acertou!")
    elif chute < numero and chute > 0:
        print("O número é mais alto")
        if (numero - 2) == chute or (numero - 1) == chute:
            print("muito perto. Errou por um ou dois números.")
    elif chute > numero and chute < 101:
        print("O número é mais baixo")
        if (numero + 2) == chute or (numero + 1) == chute:
            print("muito perto. Errou por um ou dois números.")
    else:
        print("Era necessário digitar um número entre 1 e 100")

    print("O número certo é", numero)

except:
    print("Para jogar, você só pode digitar números.")