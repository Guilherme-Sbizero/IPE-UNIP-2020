num1 = int(input("Digite e o primeiro numero: "))
num2 = int(input("Digite e o segundo numero: "))

def multiplo(a,b):
    if (b%a) == 0:
        return True
    else:
        return False

print(multiplo(num1, num2))
