''' LISTA 02 - EXERCICIO 04
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: 'Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
    Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
'''
salario = float(input("Digite o seu salario: "))
if salario > 1200:
    print("Voce deve pagar impostos!!!")
else:
    print("Voce nao deve pagar impostos!!!")