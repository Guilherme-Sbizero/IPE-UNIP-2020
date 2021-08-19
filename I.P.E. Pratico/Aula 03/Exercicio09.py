''' LISTA 02 - EXERCICIO 9
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreva um programa que leia a quantidade de dias, horas, 
    minutos e segundos do usuário. Calcule o total em segundos.
'''
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = (dias * 86400) + (horas * 3600) + (minutos * 60) + (segundos)
print("A quantidade total de segundos é: ", total)