ultimo = 0
fila = list(range(1, ultimo +1))

while True:
    print("Quantidade de clientes aguardando na fila: ",len(fila))
    print("Fila Atual: ",fila)
    print("Digite F para adicionar um cliente ao fim da fila")
    print("Digite A para realizar um atendimento, removendo um cliente da fila")
    print("Digite S para encerrar o sistema")
    operacao = input("Operacao (F, A ou S): ")
    if operacao == "A":
        if len(fila)>0:
            atendimento = fila.pop(0)
            print("Cliente ", atendimento, " atendido")
            '''print(f"Cliente {atendimento} atendido")'''
        else:
            print("Fila vazia! Ninguem para atender.")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao =="S":
        break
    else:
        print("Operacao invalida, digite apenas F, A ou S")