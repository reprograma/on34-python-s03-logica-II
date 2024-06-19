nota = float(input("Coloque a sua nota de 0 a 10: "))
if nota >= 7:
  print("aprovada")
elif nota >= 5:
  print("recuperação")
  nota_recuperacao = float(input("qual a nota da recuperação?"))
  if nota_recuperacao >= 8:
    print("Aprovada na Recuperação")
else:
  print("reprovada")
print("fim")