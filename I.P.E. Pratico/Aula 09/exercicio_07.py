def calcularIMC(pPeso, pAltura):
    pImc = (pPeso)/(pAltura**2)
    return pImc
    
def classificarIMC(pImc):
    if pImc < 18.5:
        print("Classificacao: Desnutrição")
    elif pImc < 25:
        print("Classificacao: Peso Normal")
    elif pImc < 30:
        print("Classificacao: Sobrepeso")
    elif pImc < 35:
        print("Classificacao: Obesidade Nivel I")
    else:
        print("Classificacao: Obesidade Nivel II")

def menu():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcularIMC(peso, altura)
    print("O seu IMC é:",imc)
    classificarIMC(imc)
    
menu()
