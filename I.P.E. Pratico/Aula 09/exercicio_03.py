'''3)	Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem.  
Custo: que é o custo de um item antes do imposto. '''

def somaImposto(taxaimposto, custo):
    return (0.01*taxaimposto) * custo

print(somaImposto(5,1000))  