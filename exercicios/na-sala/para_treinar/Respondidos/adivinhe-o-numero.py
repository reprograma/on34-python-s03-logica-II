#Neste programa, você precisa definir um número entre 1 e 100 e pedir para o usuário tentar acertar. 
# Você vai dizer se uma pessoa acertou, chutou muito alto ou chutou muito baixo. Diga qual o npumero#

#Atenção: esse programa só vai deixar a pessoa tentar acertar uma única vez. Na próxima semana, 
# você vai aprender a dar o quanto quiser. Esse curso só fica melhor! :D#


numero = float(input("Tente acertar. Chute um número de 1 a 100: "))

if  numero == 20:
    print("PARABÉNS VOCÊ ACERTOU!!!")

elif numero >= 21 :
    print("Chutou muito alto")

else:
    print("Chutou muito baixo")


