salario = float(input("Qual o salário? "))
vendas = float(input("Qual o valor em vendas? "))

if  vendas <= 3000:
    comissao = vendas * 0.1
elif vendas <= 5000:
    comissao = vendas * 0.15
else:
    comissao = vendas * 0.18

print("Este mês você receberá R$", salario + comissao)