'''
Esse programa tem um erro, se vc colocar os dois primeiros
números iguais, ele vai dizer que todos são iguais. O motivo é que ele 
testa tudo e sempre uma das condições é False, já que os dois primeiros são iguais.
E nosso else na linha 19, pega qualquer coisa que caia ali.
Com o que aprendeu até agora, você consegue melhorar o programa? 
'''

num1 = int(input("Entre com o primeiro número:"))
num2 = int(input("Entre com o segundo número:"))
num3 = int(input("Entre com o segundo número:"))

def maior_num(n1, n2, n3):
    if num1 > num2 and num1 > num3:
        print("O maior número é", num1)
    elif num2 > num1 and num2 > num3:
        print("O maior número é", num2)
    elif num3 > num1 and num3 > num2:
        print("O maior número é", num3)
    else:
        print("Os números são iguais")

maior_num(num1, num2, num3)