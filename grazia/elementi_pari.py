n = 3 # Lunghezza dell'array.
a = [12, 25, 1468]

c = 0
i = 0
while i < n:
	if a[i] % 2 == 0:
		c += 1
	
	i += 1

print("Ho contato " + str(c) + " numeri pari!")
