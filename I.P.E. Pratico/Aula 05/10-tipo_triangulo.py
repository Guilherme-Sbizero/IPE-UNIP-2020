a = int(input("Digite o lado a do triângulo: "))
b = int(input("Digite o lado b do triângulo: "))
c = int(input("Digite o lado c do triângulo: "))
if (a < b + c and b < a + c and c < a + b):
    if (a != b and b != c and a != c):
        print("escaleno")
    else:
        if(a == b and b == c):
            print("equilátero")
        else:
            print("isósceles")
else:
    print ("Não é um triângulo.")



