'''funcao p/ remover repetidos da lista'''
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()'''funcao sort ordena os dados dentro da lista'''
    return l

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [4,5,6,7,8,9,10,11,12,13]
listaC = listaA + listaB

listaD = remove_repetidos(listaC)

print(listaD)