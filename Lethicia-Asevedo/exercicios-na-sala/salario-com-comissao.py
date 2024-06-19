##Cálculo de salário com comissão
#A Artificia, empresa de cosméticos, te contratou para fazer um programa que calcule 
# o salário das vendedoras e elas já saibam antes quanto vão ganhar 
# com base nas vendas realizadas.

#Como vai funcionar?
#O programa deve pedir o valor do salário, o valor em vendas e calcular a 
# comissão conforme a tabela abaixo:

#Valor das vendas	Comissão
#Até R$ 3.000,00	10%
#Até R$ 5.000,00	15%
#A partir de R$ 5.000,00	18%
#Ao final, você deve mostrar algo como: Este mês você receberá R$ XXX onde XXX é a soma do salário com a comissão.


print("Olá, vamos calcular a sua comissão: ")


valor_salario = float(input("Digite o valor do seu salário: "))
valor_vendas = float(input("Digite o valor total das suas vendas neste mês: "))

calculo_comissao1 = (10 / 100) * valor_vendas
calculo_comissao2 = (15 / 100) * valor_vendas
calculo_comissao3 = (18 / 100) * valor_vendas

if valor_vendas <= 3000:
    print(f"O valor a receber desse mês é de: {calculo_comissao1 + valor_salario}")
elif valor_vendas <= 5000:
    print(f"O valor a receber desse mês é de: {calculo_comissao2 + valor_salario}")
else:
    print(f"O valor a receber desse mês é de: {calculo_comissao3 + valor_salario}")

 