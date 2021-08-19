ultimoA = 0
filaA = list(range(1, ultimoA +1))

ultimoB = 0
filaB = list(range(1, ultimoB +1))

while True:
    print("Quantidade de clientes aguardando na fila A: ",len(filaA))
    print("Quantidade de clientes aguardando na fila B: ",len(filaB))
    print("Fila Atual A: ",filaA)
    print("Fila Atual B: ",filaB)
    print("Digite F para adicionar um cliente ao fim da fila A")
    print("Digite F para adicionar um cliente ao fim da fila G")
    print("Digite A para realizar um atendimento, removendo um cliente da fila A")
    print("Digite B para realizar um atendimento, removendo um cliente da fila B")
    print("Digite S para encerrar o sistema")
    operacao = input("Operacao (F, G, A, B ou S): ")
    if operacao == "A":
        if len(filaA)>0:
            atendimentoA = filaA.pop(0)
            print("Cliente ", atendimentoA, " atendido")
        else:
            print("Fila vazia! Ninguem para atender.")
    
    elif operacao == "B":
        if len(filaB)>0:
            atendimentoB = filaB.pop(0)
            print("Cliente ", atendimentoB, " atendido")
        else:
            print("Fila vazia! Ninguem para atender.")
    
    elif operacao == "F":
        ultimoA += 1
        filaA.append(ultimoA)

    elif operacao == "G":
        ultimoB += 1
        filaB.append(ultimoB)

    elif operacao =="S":
        break
    else:
        print("Operacao invalida, digite apenas F,G, A, B ou S")