''' LISTA 03 - EXERCICIO 01
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. Caso ambos os
    números forem iguais, imprima na tela “números iguais”.
'''
a = int(input("Digite o primeiro valor numérico: "))
b = int(input("Digite o segundo valor numérico : "))
if a > b:
    print("o numero :" , a , " é o maior.")
if b > a:
    print("o numero :" , b , " é o maior.")
if a == b:
    print("Os números são iguais.")
