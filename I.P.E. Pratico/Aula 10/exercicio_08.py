lista = ['99', '102', '89', '120', '117']

cont = 0
maximo = lista[1]
while cont < 3:
    if lista[cont] > lista[cont+1]:
        maximo = lista[cont+1]
    cont = cont + 1
print(maximo)
