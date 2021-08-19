nota_lab = float(input("Digite a nota de laboratório: "))
nota_avaliacao = float(input("Digite a nota da Avaliação Semestral: "))
nota_exame = float(input("Digite a nota do Exame Final: "))
media = ((nota_lab * 0.2) + (nota_avaliacao * 0.3) + (nota_exame * 0.5))
if (media > 8):
    print ("Media =",media,"- Conceito A")
elif (media > 7):
    print ("Media =",media,"- Conceito B")
elif (media > 6):
    print ("Media =",media,"- Conceito C")
elif (media > 5):
    print ("Media =",media,"- Conceito D")
else:
    print ("Media =",media,"- Conceito E")


