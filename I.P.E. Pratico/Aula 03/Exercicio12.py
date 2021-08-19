''' LISTA 02 - EXERCICIO 12
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreva um programa que calcule o tempo de uma viagem de carro. 
    Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = float(input("Digite a distancia da viagem em km: "))
velocidade = float(input("Digite a velocidade media da viagem: "))
tempo = (distancia/velocidade)
print("O tempo da viagem foi de: ",tempo," horas")