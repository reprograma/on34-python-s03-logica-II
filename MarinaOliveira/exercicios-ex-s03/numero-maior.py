print("~~~~  " "QUAL O MAIOR NÚMERO?" "  ~~~~\n")

num1 = int(input("Digite o primeiro número de 0 a 100: "))
num2 = int(input("Digite o segundo número de 0 a 100: "))
num3 = int(input("Digite um terceiro número de 0 a 100: "))



if num1 > num2 and num3:
    maior_numero = num1

elif num1 < num2 > num3:
    maior_numero = num2

else:
    maior_numero = num3

print(f"O maior número é {maior_numero}")    