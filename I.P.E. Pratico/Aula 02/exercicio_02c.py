''' LISTA 01 - EXERCICIO 02C
    Nome: Guilherme Augusto Sbizero Correa
    Data: Agosto/2020
    Enunciado:
    Resolva as expressões matemáticas manualmente no caderno, após, 
    converta as seguintes expressões matemáticas para que possam ser 
    calculadas usando o interpretador Python (confirmando o resultado
    encontrado manualmente).
    c) (9^4 + 2) * 6 - 1

'''
#Maneira 01:
#print((9**4+2)*6-1)

#Maneira 02:
#a = 9
#b = 4
#c = 2
#d = 6
#e = 1
#print((a**b+c)*d-e)

#Maneira 03:
a = int(input("Entre com a variavel a [int]:"))
b = int(input("Entre com a variavel b [int]:"))
c = int(input("Entre com a variavel c [int]:"))
d = int(input("Entre com a variavel d [int]:"))
e = int(input("Entre com a variavel e [int]:"))
print((a**b+c)*d-e)