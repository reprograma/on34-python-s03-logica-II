#Custo de Viagem

def calc_viagem(km):
    custofixo = 20.00
    if km <= 200:
        valor_por_km = 0.75
    elif 200 < km <= 500:
        valor_por_km = 0.60
    else:
        valor_por_km = 0.50

    total = custofixo + (km * valor_por_km)
    print("Sua viagem com ", km ," km custará R$ ", total)

km_viajados = input("Digite a distância em km da viagem: ")

try:
    km = float(km_viajados)
    if 0 <= km < 50:
        print("Alerta!! A vida é muito curta, e sua viagem tambem! A viagem deve ser de pelo menos 50 km.")
    elif km < 0:
        print("Alerta!! Não me faz andar prá tras e nem ficar parado! A distância inserida não pode ser negativa.")
    else:
        calc_viagem(km)
except:
    print("Seus caracteres são especiais demais pro meu programa :( Por favor, insira um número :)")
   


