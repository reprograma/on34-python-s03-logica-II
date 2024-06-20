# Custo da viagem exercício para casa semana 03 


def custo_fixo ():
    x = 20
    return x 
    
def km_200 (y):
    km_200 = (custo_fixo() + (y * 0.75))
    return km_200

def km_500 (y):
    km_500 = (custo_fixo() + (y * 0.60))
    return km_500

def km_maior_500 (y):
    km_maior_500 = (custo_fixo() + (y * 0.50))
    return km_maior_500

try:
    print("Olá! Aqui você encontra viagens de ônibus baratas a partir de R$57,5.")
    km = float(input("Para calcular o valor da sua viagem, por favor, informe a quilometragem da viagem desejada: "))

    if km < 0:
        print("Você não pode digitar uma quilometragem negativa!")

    elif km < 50:
        print("Sua viagem com ", km, "km", "não pode ser calculada. Nossas viagens são a partir de 50km! Obrigada pela compreensão")
    
    elif km <= 200:
        print("Sua viagem com ", km, "km", "custará R$", km_200(y= km))
    
    elif km <= 500:
        print("Sua viagem com ", km, "km", "custará R$", km_500(y= km))

    else:
        print("Sua viagem com ", km, "km", "custará R$", km_maior_500(y= km))

except:
    print("Você deve informar um número a partir de 50. Letras e caracteres especiais não são aceitos.")
   


