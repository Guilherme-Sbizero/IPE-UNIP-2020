cor = input("Digite a cor do selo:")
qtde = int(input("Digite a quantidade do produto:"))
if (cor == 'verde'):
    print ("O valor do produto é:",5.5 * qtde)
elif (cor == 'azul'):
    print ("O valor do produto é:",5.7 * qtde)
elif (cor == 'branco'):
    print ("O valor do produto é:",4 * qtde)
elif (cor == 'rosa'):
    print ("O valor do produto é:",3.5 * qtde)
else:
    print ("Digite uma cor válida!")
