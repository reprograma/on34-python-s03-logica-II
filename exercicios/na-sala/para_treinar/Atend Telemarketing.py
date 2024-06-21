print("Olá! Obrigada por ligar para nós.")
print("Para falar com Financeiro, digite 1.")
print("Para falar com Administrativo, digite 2.")
print("Para falar com Recursos Humanos, digite 3.")
print("Para falar com Assistência Técnica, digite 4.")

try:
    opcao = int(input("Digite o número correspondente à área que deseja falar: "))

    if opcao == 1:
        print("Você será direcionada para o Financeiro.")
    elif opcao == 2:
        print("Você será direcionada para o Administrativo.")
    elif opcao == 3:
        print("Você será direcionada para o Recursos Humanos.")
    elif opcao == 4:
        print("Você será direcionada para a Assistência Técnica.")
    else:
        print("Opção inválida. Por favor, você deve digitar um número entre 1 e 4.")

except:
    print("Você não pode colocar caracteres que não sejam números de 1 a 4")