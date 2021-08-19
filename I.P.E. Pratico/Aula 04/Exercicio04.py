''' LISTA 03 - EXERCICIO 04
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreve um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
    Para salários superiores a R$ 1250,00, calcule um aumento de 10%. 
    Para os inferiores ou iguais, de 15%.
'''
salario = float(input('Digite o salario do funcionario: '))
if salario > 1250:
    aumento = salario *0.1
else:
    aumento = salario *0.15

print("O aumento é de: ",aumento)

