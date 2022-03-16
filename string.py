# https://realpython.com/python-f-strings/#simple-syntax

import os
os.system("clear")

pi = 3.14

# Cast esplicito a stringa per poter essere concatenato
print("pi: " + str(pi))

# Indicizzazione dal primo carattere
something = "python"
print(something[0])

# Si può indicizzare anche partendo dall'ultimo carattere mettendo indici negativi.
# ultimo carattere:
print(something[-1])

# Tutti i caratteri dal 2 al 4
print(something[2:4])

# Stampa formattata:
# C like
print("str: %s, di nuovo: %s!" % (something, something))

# str.format(): vecchio modo python
print("str: {}!".format(something))
print("str: {nome_linguaggio}!".format(nome_linguaggio=something))

# F: nuovo modo python
print(F"str: {something}!")
print(f"str: {something}!")

# Stringa multiriga
multiriga = f"""
Una
Stringa
Multiriga
pi: {pi}
"""

print(multiriga)

# Lunghezza di una stringa
print(str(len(multiriga)) + "\n")


# Per verificare la presenza di una sottostringa in una stringa
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
