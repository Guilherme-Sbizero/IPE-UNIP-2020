temp = [-10, -8, 0, 1, 2, 5, -2, -4]

cont = 0
minimo = temp[0]
while cont < 7:
    if minimo > temp[cont+1]:
        minimo = temp[cont+1]
    cont = cont + 1
print("A temperatura mínima é: ", minimo)

cont = 0
maximo = temp[0]
while cont < 7:
    if maximo < temp[cont+1]:
        maximo = temp[cont+1]
    cont = cont + 1
media = (minimo + maximo)/2

print("A temperatura máxima é: ", maximo)
print("A temperatura média é: ", media)
