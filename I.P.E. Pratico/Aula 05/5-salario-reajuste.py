salario = float(input("Digite o salario:"))
if (salario < 500):
    novo_salario = salario * 1.15
else:
    if (salario <= 1000):
        novo_salario = salario * 1.1
    else:
        novo_salario = salario * 1.05
print ("O salário reajustado é:", novo_salario)
