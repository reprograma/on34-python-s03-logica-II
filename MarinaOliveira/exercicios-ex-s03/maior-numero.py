numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

def maior(x, y):
    if x > y:
     print("O primeiro valor digitado,", x, ", é maior que o segundo valor digitado", y,".")
    elif x == y:
     print("Ambos os valores digitados", x, "e", y, "são iguais.")
    else:
        print("O segundo valor digitado,", y, ", é maior que o primeiro valor digitado", x, ".")

maior(numero1, numero2)