''' LISTA 02 - EXERCICIO 6
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreva uma expressão que será utilizada para decidir se um aluno 
    foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser 
    maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota 
    de cada uma está armazenada nas seguintes variáveis: materia1, materia2,
materia3.
'''
'''interpretação 01
materia1 = float(input("Digite a nota da materia 1: "))
materia2 = float(input("Digite a nota da materia 2: "))
materia3 = float(input("Digite a nota da materia 3: "))
media = (materia1 + materia2 + materia3)/3
if media > 7:
    print("O aluno esta aprovado, com media: ",media)
else:
    print("O aluno esta reprovado, com media: ",media)

'''
materia1 = float(input("Digite a nota da materia 1: "))
materia2 = float(input("Digite a nota da materia 2: "))
materia3 = float(input("Digite a nota da materia 3: "))

if (materia1 > 7) and (materia2 > 7) and (materia3 > 7):
    print("O aluno esta aprovado")
else:
    print("O aluno esta reprovado")
