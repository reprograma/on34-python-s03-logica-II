##Olha a multa!
#O Departamento de Trânsito da sua cidade te contratou para fazer um programa que diga
#  se o carro passou dentro da velocidade permitida ou acima da velocidade. 
# Se ele passar acima da velocidade máxima permitida, calcule a multa. 
# Para até 20% acima da velocidade máxima permitida, o valor é de R$ 200 e, 
# acima disso, o valor é de R$ 350.

#Além da velocidade do veículo, você deve solicitar a velocidade máxima da via.

#Bônus: faça o programa com função (def) para facilitar, 
# já que o Departamento de Trânsito precisará calcular a velocidade de todos 
# os carros que estão passando naquela via (e serão muitos!).


print("Olá, vamos calcular o valor da sua multa")

velocidade_real = int(input("Digite a velocidade que você passou: "))
velocidade_permitida = int(input("Digite a velocidade máxima permitida pela via: "))

def calculo_multa():
    if velocidade_real > velocidade_permitida:
        print(f"Ops, você excedeu o limite de velocidade, o valor da sua multa é de R${(velocidade_permitida /100)* 20}")
    else:
        print("Parabéns, você estava dentro do limite de velocidade e não obteve multas !!!")


calculo_multa()





