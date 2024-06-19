print("### " "CÁLCULO DE SALÁRIO" " ###\n")

def calcular_comissao():

 salario_fixo = float(input("Por favor, digite o salário fixo R$: "))
 vendas = float(input("Digite o valor das vendas R$: "))


 if vendas <= 3000:
    comissao = vendas * 0.10

 elif vendas <= 5000:
    comissao = vendas * 0.15

 else:
    comissao = vendas * 0.18

 salario_total = salario_fixo + comissao

 print(f"Este mês você receberá R$ {salario_total:.2f}")

calcular_comissao()  


