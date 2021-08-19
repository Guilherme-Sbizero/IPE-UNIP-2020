num1 = int(input("Digite a base de um triangulo: "))
num2 = int(input("Digite a altura de um triangulo: "))


def area(base, altura):
    resultado = (base * altura)/2
    return resultado

print(area(num1,num2))
