dep = float(input("Digite o valor do depósito: "))
jur = float(input("Digite o valor dos juros: "))

meses = 0

print("Valor inicial do depósito: ", dep)

while (meses < 24):
    
    dep = dep * (1 + (jur * 0.01))
    print("O valor do depósito no mês ", meses + 1, "será de:", dep)
    novo = float(input("Qual o valor que deseja depositar esse mês?"))
    dep = dep + novo
    meses = meses + 1
