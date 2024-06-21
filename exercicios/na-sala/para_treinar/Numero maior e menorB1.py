num1 = int(input("Entre com o primeiro número:"))
num2 = int(input("Entre com o segundo número:"))

def maior_num(n1, n2):
    if num1 > num2:
        print("O maior número é", num1)
    elif num1 < num2:
        print("O maior número é", num2)
    else:
        print("Os números são iguais")

maior_num(num1, num2)
