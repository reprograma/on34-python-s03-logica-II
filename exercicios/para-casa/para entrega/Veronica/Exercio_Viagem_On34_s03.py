#Entrada de dados
try:
    km = float(input("Qual é a quilometragem desta viagem? Digite um número igual ou maior que cinquenta."))

except:
    print("Digite um número...")

#Função que calcula o valor da viagem
def viagem(km):
    if km >= 50:
        if km <= 200:
            print("A viagem terá um adicional de 0,75 centavos por quilometro")

            taxa_viagem = 0.75 * km

        elif km > 200 and km <= 500:
            print("A viagem terá um adicional de 0,60 centavos por quilometro")

            taxa_viagem = 0.60 * km

        else:
            print("A viagem terá um adicional de 0,50 centavos por quilometro")

            taxa_viagem = 0.50 * km
        custo_viagem = taxa_viagem + 20
        print("sua viagem com", km, " custará R$", custo_viagem )

    else:
        print("Não aceitamos viagens com menos de 50 quilometros...")

viagem(km)




