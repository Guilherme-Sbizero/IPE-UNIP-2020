''' LISTA 02 - EXERCICIO 10
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Faça um programa que calcule o aumento de um salário. 
    Ele deve solicitar o valor do salário e a porcentagem do aumento. 
    Exiba o valor do aumento e do novo salário.
'''

salario = float(input("Digite o salario: "))
aumento = float(input("Digite o % de aumento: "))
aumentoValor = (salario * aumento)/100
novoSalario = salario + aumentoValor
print("O aumento foi de: ",aumentoValor, " e o novo salario atualizado é: ",novoSalario)