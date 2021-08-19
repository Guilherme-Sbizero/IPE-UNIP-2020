'''
Escreva a função vogal que recebe um único caractere como parâmetro e devolve 
True se ele for uma vogal e False se for uma consoante.
Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings
Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, 
ou seja, precisa estar entre aspas.
'''
letra = input("Digite uma vogal: ")

def vogal(letra):
    codigoAscii = ord(letra)
    if codigoAscii == 65:
        return True
    if codigoAscii == 69:
        return True
    if codigoAscii == 73:
        return True
    if codigoAscii == 79:
        return True
    if codigoAscii == 85:
        return True
    if codigoAscii == 97:
        return True
    if codigoAscii == 101:
        return True
    if codigoAscii == 105:
        return True
    if codigoAscii == 111:
        return True
    if codigoAscii == 117:
        return True
    else:
        return False

print(vogal(letra))

