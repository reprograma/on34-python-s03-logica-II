'''Você já deve ter ligado em uma empresa e ouvido uma lista de opções com números que deviam ser digitados com a 
opção escolhida para ser direcionada a um certo departamento. Seu trabalho agora é criar um minissistema de telemarketing.

Como vai funcionar?
O programa vai mostrar na tela as opções e, dependendo do número digitado, a pessoa vai ser direcionada a um outro 
atendimento. Ao final, ficará assim:

Olá! Obrigada por ligar para nós Para falar com Financeiro, digite 1. Para falar com Administrativo, 
digite 2. Para falar com Recursos Humanos, digite 3. Para falar com Assistência Técnica, digite 4.

Dependendo da resposta, o programa vai mostrar na tela uma frase diferente. Por exemplo: Ao responder 1, 
vai aparecer a frase: Você será direcionada para o Financeiro.

Bônus
Após ser direcionada para o departamento, pergunte: se a pessoa quer deixar um recado para o (nome do departamento) 
ou falar com atendente. caso a pessoa escolha deixar recado, imprima: "Você pode deixar seu recado agora". 
Caso ela escolha falar com atendente, imprima: "Por favor, aguarde seu atendimento".'''

menu = int(input("Olá! Obrigada por ligar para nós.Para falar com Financeiro, digite 1. Para falar com Administrativo, digite 2. Para falar com Recursos Humanos, digite 3. Para falar com Assistência Técnica, digite 4: "))


if menu == 1:
    print("Você será direcionada para o Financeiro")

    departamento = input("Digite 1 se a senhora(o) gostaria de deixar um recado para o Financeiro, ou digite 2 para falar com atendente: ")
    if departamento == 1:
        print("Você pode deixar seu recado agora")
    else:
        print("Por favor, aguarde seu atendimento")

elif menu == 2:
    print("Você será direcionada para o Administrativo")

    departamento = input("Digite 1 se a senhora(o) gostaria de deixar um recado para o Administrativo, ou digite 2 para falar com atendente: ")
    if departamento == 1:
        print("Você pode deixar seu recado agora")
    else:
        print("Por favor, aguarde seu atendimento")

elif menu == 3:
    print("Você será direcionada para o Recursos Humanos")

    departamento = input("Digite 1 se a senhora(o) gostaria de deixar um recado para o Recursos Humanos, ou digite 2 para falar com atendente: ")
    if departamento == 1:
        print("Você pode deixar seu recado agora")
    else:
        print("Por favor, aguarde seu atendimento")

else:
    print("Você será direcionada para o Assistência Técnica")

    departamento = input("Digite 1 se a senhora(o) gostaria de deixar um recado para o Financeiro, ou digite 2 para falar com atendente: ")
    if departamento == 1:
        print("Você pode deixar seu recado agora")
    else:
        print("Por favor, aguarde seu atendimento")
