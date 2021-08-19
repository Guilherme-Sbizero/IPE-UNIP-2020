'''2)	Faça um programa, com uma função que necessite de um argumento. A função retorna o 
valor de caractere ‘P’, se seu argumento for positivo, 
e ‘N’, se seu argumento for zero ou negativo.'''

def pn(x):
    if x < 0:
        return "N"
    elif x > 0:
        return "P"
    else:
        return "0"

num = int(input("Digite um numero: "))
print(pn(num))