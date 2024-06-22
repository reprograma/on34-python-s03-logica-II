
try:
    def viagem (km_viajado):
        if km_viajado < 50:
            print("Infelizmente nosso sistema não calcula viagens cuja quilometragem viajada é inferior a 50km. :(")
        
        elif km_viajado <= 200:
            valor_adicional = 0.75
            valor_total = 20+km_viajado*valor_adicional
            print("Sua viagem com", km_viajado, "kms terá o valor de", valor_total, "reais.")

        elif km_viajado <= 500:
            valor_adicional = 0.6
            valor_total = 20+km_viajado*valor_adicional
            print("Sua viagem com", km_viajado, "kms terá o valor de", valor_total, "reais.")
        else:
            valor_adicional = 0.5
            valor_total = 20+km_viajado*valor_adicional
            print("Sua viagem com", km_viajado, "kms terá o valor de", valor_total, "reais.")

    viagem(float(input("Boa tarde! Gostaria de saber quanto ficou sua viagem? Digite quantos km foram viajados no total, lembrando que nosso sistema não \naceita caracteres especiais, tampouco letras:")))

except:  
     print("Lembre-se, nosso sistema não aceita caracteres especiais nem letras :) Por favor, tente novamente.")
    

    
    