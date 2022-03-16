# https://realpython.com/python-f-strings/#simple-syntax

from audioop import mul
import os
os.system("clear")

pi = 3.14

# Cast esplicito a stringa per poter essere concatenato
print("pi: " + str(pi))

# Indicizzazione dal primo carattere
str = "python"
print(str[0])

# Si può indicizzare anche partendo dall'ultimo carattere mettendo indici negativi.
# ultimo carattere:
print(str[-1])

# Tutti i caratteri dal 2 al 4
print(str[2:4])

# Stampa formattata:
# C like
print("str: %s, di nuovo: %s!" % (str, str))

# str.format(): vecchio modo python
print("str: {}!".format(str))
print("str: {nome_linguaggio}!".format(nome_linguaggio=str))

# F: nuovo modo python
print(F"str: {str}!")
print(f"str: {str}!")

# Stringa multiriga
multiriga = f"""
Una
Stringa
Multiriga
pi: {pi}
"""

print(multiriga)
