''' LISTA 03 - EXERCICIO 07
    Nome: Guilherme Augusto Sbizero Correa
    Data: Setembro /2020
    Enunciado: Escreva um programa que calcular a categoria de um produto e determine o preço pela tabela: 
    Categoria 1 valor de R$ 10,00; Categoria 2 valor de R$ 15,00; Categoria 3 valor de R$ 19,00; 
    Categoria 4 valor de R$ 23,00 e Categoria 5 valor de R$ 27,00.
'''
print("Categorias")
print("Categoria 1 - Valor R$ 10,00")
print("Categoria 2 - Valor R$ 15,00")
print("Categoria 3 - Valor R$ 19,00")
print("Categoria 4 - Valor R$ 23,00")
print("Categoria 5 - Valor R$ 27,00")

categoria = int(input('Digite o número da categoria escolhida:'))
if categoria == 1:
    produto = 10
elif categoria == 2:
    produto = 15
elif categoria == 3:
    produto = 19
elif categoria == 4:
    produto = 23
elif categoria == 5:
    produto = 27
else:
    print("Digite uma categoria valida!!!")
    produto = "invalido"
print("O produto escolhido custa: R$ ",produto)




