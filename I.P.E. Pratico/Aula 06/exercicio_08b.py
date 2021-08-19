soma = 0
i = 0
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print("Soma: ")

'''while (i != n1):
    soma = soma + n2
    print(" + ",n2)
    i = i + 1'''

for i in range (n1):
    soma = soma + n2
    print(" + ",n2)

print("= ", soma)


