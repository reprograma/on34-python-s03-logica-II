gasto_fixo = 20
texto = 'Boas Vindas à ReproViagens 🚌'
texto1 = 'Nos diga sua km e te diremos o valor 😉'

def calculo_total(km_viajado):
    if km_viajado <= 200:
        return km_viajado * 0.75
    elif km_viajado <= 500:
        return km_viajado * 0.60
    else:
        return km_viajado * 0.50
    
    
print('-='*30)
print(texto.center(60))
print(texto1.center(60))
print('-='*30, '\n')

try:
    km_viajado = float(input('Quantos Km serão rodados na viagem?: '))

    if km_viajado < 0:
        print('Erro ao calcular a quilometragem. Tente novamente.\n')
    elif km_viajado < 50:
        print('Não fazemos viagens com menos de 50 km para percorrer.\n')
    else:
        custo_km = calculo_total(km_viajado)
        valor_total = custo_km + gasto_fixo
        print(f'Com o total de {km_viajado:.2f} km percorridos, sua viagem terá o custo final de R$ {valor_total:.2f} reais.\n')     

except ValueError:
    print('Insira apenas números válidos.\n')

texto2 = 'FIM'

print('-='*30)
print(texto2.center(60))
print('-='*30)
