#Custo de viagem =20,00 cada + valor referente aos km viajados
'''
kms viajados	valor por km
Até 200km	R$ 0,75
Até 500km	R$ 0,60
mais de 500km	R$ 0,5
'''
'''
Calcule o valor e imprima a resposta como: Sua viagem com XX km custará R$ YY onde XX é o número de quilômetros e Y é o valor total a ser pago.

Seu programa não pode deixar o usuário:

calcular viagens com menos de 50km;
entrar com números negativos;
entrar com letras ou caracteres especiais que podem quebrar o programa.
Bônus: use função ;)
'''
'''
custo_viagem = 20
ateduzentos_km = 0.75
meio_km = 0.60
maisde_meiokm = 0.5 
'''
dist_usuario = float(input("Para saber o valor da sua viagem, digite o número correpondente a distância:"))


viagem1 = dist_usuario * (0.75 + 20)
viagem2 = dist_usuario * (0.60 + 20)
viagem3 = dist_usuario * (0.5 + 20)


try:
   
    if dist_usuario == int(input()):
        print("Ingresse somente números. Tente novamente!")
    elif dist_usuario <50:
        print("Para que a sua passagem seja calculada, a distância deve ser maior que 50km. Tente novamente.")
    elif dist_usuario <0:
        print("Para que a sua passagem seja calculada, ingresse números positivos. Tente novamente.")
    elif dist_usuario >0 and dist_usuario <=200:
        print("Sua viagem de", dist_usuario, "km custará R$", viagem1)
    elif dist_usuario >200 and dist_usuario <= 500:
        print("Sua viagem de", dist_usuario, "km custará R$", viagem2)
    elif dist_usuario > 500:
        print("Sua viagem de", dist_usuario, "km custará R$", viagem3)
    else: 
        print("Opção inválida. Tente novamente!")
except:
    print("Fim")


