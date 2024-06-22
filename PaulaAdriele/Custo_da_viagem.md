# Custo da viagem
"""
Uma empresa de viagens de ônibus contratou você para fazer um programa que calcule o preço das viagens. 
Cada viagem custa R$ 20,00 e mais um valor referente aos quilômetros viajados, conforme a tabela abaixo:

| kms viajados | valor por km |
| --- | --- |
| Até 200km | R$ 0,75 |
| Até 500km | R$ 0,60 |
| mais de 500km | R$ 0,50 |

Calcule o valor e imprima a resposta como:
**Sua viagem com XX km custará R$ YY**
onde XX é o número de quilômetros e Y é o valor total a ser pago.

Seu programa não pode deixar o usuário:
- calcular viagens com menos de 50km;
- entrar com números negativos;
- entrar com letras ou caracteres especiais que podem quebrar o programa.
"""

print("\n------------------------------------------\nOlá, como está o seu dia hoje? ☀️\nVamos calcular o custo da sua viagem?✈️\n------------------------------------------")

while True:
    try:
        quilometros = float(input("Qual a quilometragem da sua viagem?"))
        preco_base = 20

        if  quilometros <= 49:  
            print("\n------------------------------------------\nOps❗ Não calculamos viagens com menos de 50Km ou com valores negativos.😬\n\nTente novamente\n------------------------------------------")
        
        elif 50 <= quilometros <= 200:
            preco = preco_base + (quilometros*0.75)
            preco = round(preco,2)
            print("\n------------------------------------------\nSua viagem de",quilometros,"km, custará R$",preco,"\n--------------Boa viagem ✈️--------------")
            break
            
        elif 201 <= quilometros <= 499:
            preco = preco_base + (quilometros*0.60)
            preco = round(preco,2)
            print("Sua viagem de",quilometros,"km, custará R$",preco,"\n--------------Boa viagem ✈️--------------")
            break

        else: #quilometros >= 500
            preco = preco_base + (quilometros*0.50)
            preco = round(preco,2)
            print("Sua viagem de",quilometros,"km, custará R$",preco,"\n--------------Boa viagem ✈️--------------")
            break
            


    except:
        print ("\nOps❗ Acho que não consegui te entender.\nGaranta que seus quilômetros sigam os seguintes critérios\n🚩 Número positivos\n🚩 Utilize (.) ponto como separador\n🚩 Tenha mais de 50km\n\nTente novamente.\n------------------------------------------")

