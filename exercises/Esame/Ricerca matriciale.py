A = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
cercato = 7

trovato = False

i = 0
while i<len(A) and not trovato:

	j = 0
	while j<len(A[i]) and not trovato:
		if A[i][j] == cercato:
			trovato = True
		
		j += 1
	i += 1

# Fuori dal ciclo, si decrementa i di 1 per poter rintracciare l'eventuale elemento trovato.
i -= 1
j -= 1

if trovato:
	print("Ho trovato " + str(cercato) + " alla posizione [" + str(i) + ", " + str(j) + "]")

else:
	print("Non l'ho trovato...")
