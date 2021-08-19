lista = ['99', '102', '89', '120', '117']

cont = 0
minimo = lista[1]
while cont < 3:
    if lista[cont] > lista[cont+1]:
        minimo = lista[cont+1]
    cont = cont + 1
print(minimo)
