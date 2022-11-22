x = float(input("Inserisci il valore di x: "))
y = float(input("Inserisci il valore di y: "))
operazione = input("Inserisci l'operazione desiderata (+, -, *, /): ")

if operazione == "+":
	risultato = x + y

elif operazione == "-":
	risultato = x - y

elif operazione == "*":
	risultato = x * y

elif operazione == "/":
	risultato = x / y

else:
	print(operazione + " non è un operatore valido!")
	exit(1)

print("Il risultato di " + str(x) + operazione + str(y) + " è " + str(risultato))

