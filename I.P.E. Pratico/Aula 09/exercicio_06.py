'''6)	Ler o estado civil de quinze pessoas e mostrar a quantidade de pessoas casadas.'''

soma = 0
for contador in range(1,16):
    estado_civil = input("Digite o estado civil da pessoa C ou S: ")
    estado_civil = estado_civil.upper()
    if(estado_civil == "C"):
        soma = soma + 1

print("A quantidade de pessoas casadas é: ",soma)
    