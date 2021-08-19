''' LISTA 01 - EXERCICIO 06
    Nome: Guilherme Augusto Sbizero Correa
    Data: Agosto/2020
    Enunciado:
    Escreva o programa que receba o valor do salário, 
    do aumento (%) e calcule o valor do novo salário.
    Considere o salário de R$ 750,00 e o aumento de 15%.
'''
#Entrada de Dados:
salario = float(input("Entre com o salario [R$]: "))
aumento = float(input("Entre com o aumento [ %]: "))

#Processamento:
novoSalario = salario + (salario*(aumento/100))

#Saida:
print("O novo salario do funcionario com aumento de ",aumento," %"," é de R$ ",novoSalario)