# Scrivere l'algo di input
# Implementare limiti n, m, r, s
# Implementare algo di ricerca
# Implementare funzione di confronto tra matrici 2x3
# 	La funzione deve essere del tipo f: N^4 -> {True, False}

# Mostrare output del risultato

# Funzione di confronto.
def confrontaMatrici(i_offset, j_offset, k_offset, h_offset):
	esatti = 0

	for i in range(ROWS):
		for j in range(COLS):
			if A[i_offset + i][j_offset + j] == B[k_offset + i][h_offset + j]:
				esatti += 1
	
	if esatti == ROWS * COLS:
		return True
	
	return False

# Righe e colonne della sotto matrice da ricercare.
ROWS = 2
COLS = 3

# Input
n = int(input("Inserisci n: "))		#Dimensioni matrice A.
m = int(input("Inserisci m: "))

r = int(input("Inserisci r: "))		#Dimensioni matrice B.
s = int(input("Inserisci s: "))

assert(n >= ROWS and r >= ROWS and m >= COLS and s >= COLS)

A = []
B = []

for i in range(n):
	tmp = []
	for j in range(m):
		tmp.append(
			int(input("Inserisci A[" + str(i) + "][" + str(j) + "]: "))
		)
	
	A.append(tmp)

for i in range(r):
	tmp = []
	for j in range(s):
		tmp.append(int(input("Inserisci B[" + str(i) + "][" + str(j) + "]: ")))
	
	B.append(tmp)

# Algoritmo di ricerca
trovato = False
for i in range(n - ROWS + 1):
	for j in range(m - COLS + 1):
		for k in range(r - ROWS + 1):
			for h in range(s - COLS + 1):
				if confrontaMatrici(i, j, k, h):
					trovato = True

if trovato:
	print("Ho trovato due sotto matrici coincidenti.")

else:
	print("Non ho trovato due sotto matrici coincidenti.")
