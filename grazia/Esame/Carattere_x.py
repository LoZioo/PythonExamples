lista = ["ciao", "come", "stai", "xxx"]

trovato = False
for str in lista:
	if 'x' in str:
		trovato = True

if trovato:
	print("Trovato!")

else:
	print("Non trovato...")
