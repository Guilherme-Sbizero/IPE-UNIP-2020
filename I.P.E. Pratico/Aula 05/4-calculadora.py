x = float(input("Digite o primeiro número:"))
y = float(input("Digite o segundo número:"))
sinal = input("Digite a operação:")
if (sinal == '+'):
    print (x,sinal,y,"=",x + y)
elif (sinal == '-'):
    print (x,sinal,y,"=",x - y)
elif (sinal == '*'):
    print (x,sinal,y,"=",x * y)
elif (sinal == '/'):
    if (y == 0):
        print ("Impossível divisão por zero!")
    else:
        print (x,sinal,y,"=",x / y)
else:
    print ("Favor informar um sinal válido.")
