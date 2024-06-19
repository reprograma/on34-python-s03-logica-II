#Resultado do IMC
#Você já conheceu o cálculo do IMC e agora precisa montar um programa que peça o nome da pessoa, 
# o peso em quilos e a altura em metros. Será necessário mostrar o resultado com base na tabela 
# da OMS (Organização Mundial de Saúde):

#IMC	Classificação
#Abaixo de 18,5	Magreza
#Entre 18,5 e 24,9	Normal
#Entre 25,0 e 29,9	Sobrepeso
#Entre 30,0 e 39,9	Obesidade
#Maior que 40,0	Obesidade grave

#Como vai funcionar?
#Dependendo do valor do IMC, o programa precisa responder qual a classificação da pessoa. 
# A saída deve ser assim: Oi, Fulana! Sua classificação é de XXX. 
# onde Fulana é o nome e XXX é a interpretação, conforme a tabela acima.

#Obs.1: O IMC é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado.

#Obs.2: A potência é calculada com ** (dois asteriscos). Por exemplo, 2 elevado à terceira fica 2 ** 3.

print ("Olá, vamos calcular o seu IMC")

nome = input("Por favor, digite aqui o seu primeiro nome: ")
peso = float(input("Agora digite o seu peso por favor: "))
altura = float(input("Por último, digite a sua altura por favor: "))

calculo_imc = (peso / altura)** 2

if calculo_imc < 18.5:
    print(f"Olá {nome}, a classificação do seu IMC é: Magreza")
elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
    print(f"Olá {nome}, a classificação do seu IMC é: Normal) ")
elif calculo_imc >= 25.0 and calculo_imc <= 29.9:
    print(f"Olá {nome}, a classificação do seu IMC é: Sobrepeso.")
elif calculo_imc >= 30.0 and calculo_imc <= 39.9:
    print(f"Olá {nome}, a classificação do seu IMC é: Obesidade")
else:
    print(f"Olá {nome}, a classificação do seu IMC é: Obesidade grave")
