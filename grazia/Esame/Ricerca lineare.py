A = [1, 2, 3]
cercato = 1

# Da qui'
i = 0
trovato = False
while i<len(A) and not trovato:
	if A[i] == cercato:
		trovato = True

	i += 1

# Fuori dal ciclo, si decrementa i di 1 per poter rintracciare l'eventuale elemento trovato.
i -= 1

if trovato:
	print("L'ho trovato alla posizione " + str(i))

else:
	print("Non l'ho trovato...")
