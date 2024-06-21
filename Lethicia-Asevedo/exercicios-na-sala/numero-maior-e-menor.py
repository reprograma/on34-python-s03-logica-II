#Qual o maior número?
#Faça um programa que peça dois números inteiros de 0 a 100 e imprima o maior.

#A saída deve ser parecida com isso: O maior número é X sendo que X deve ser o maior número dado pelo usuário.

#Bônus1: tente fazer como função.

#Bônus2: peça para o usuário 3 números e diga o mais alto.


print("Olá! Vamos adivinhar qual é o número maior?")

num1 = int(input("Digite aqui o primeiro número: "))
num2 = int(input("Digite aqui o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o {num2}")
elif num2 == num1:
    print(f"Os números {num1} e {num2} são iguais !")
else:
    print(f"O número {num2} é maior que o número {num1}")


