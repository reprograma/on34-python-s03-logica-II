'''
Esse programa funciona, mas... se a pessoa digita a primeira opção 
errado, ele dá continuidade sem a escolha do departamento.
Então funciona, só que não...
'''

print("Olá! Obrigada por ligar para nós.")
print("Para falar com Financeiro, digite 1.")
print("Para falar com Administrativo, digite 2.")
print("Para falar com Recursos Humanos, digite 3.")
print("Para falar com Assistência Técnica, digite 4.")

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

opcao_dep = int(input("Digite 1 para deixar um recado ou 2 para falar com um atendente "))
if opcao_dep == 1:
    print("Você pode deixar seu recado agora.")
elif opcao_dep == 2:
    print("Por favor, aguarde seu atendimento.")
else:
    print("Opção inválida. Por favor, você deve digitar 1 ou 2.")