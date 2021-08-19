dividendo = int(input("Digite o primeiro numero: "))
divisor = int(input("Digite o segundo numero: "))

quociente = 0

aux = dividendo 

while aux >= divisor:
    aux = aux - divisor
    quociente = quociente + 1

resto = aux

print("Resultado :", quociente)
print("Resto:     ", resto)




