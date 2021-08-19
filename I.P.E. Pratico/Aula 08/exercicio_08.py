numero = int(input("Digite um número:"))
divisor = 2
primo = True
while divisor < numero and primo:
	resto = numero % divisor
	if (resto == 0):
		primo = False
	divisor = divisor + 1
if primo and numero != 1:
	print ("primo")
else:
	print ("não primo")

