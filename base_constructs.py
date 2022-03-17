# if
from pydoc import doc


a = 200
b = 33

if b > a:
  print("b is greater than a")

elif a == b:
  print("a and b are equal")
	
else:
  print("a is greater than b")

# if aritmetico
if a > b: print("A")

# if-else aritmetico
print("A") if a > b else print("B")

# if-else if-else aritmetico
print("A") if a > b else print("=") if a == b else print("B")

# while
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1

else:
  print("i is no longer less than 6\n")

# for
# Si genera un insieme di numeri sul quale fare il for each...
# Anche quì, funziona l'else per eseguire codice appena la condizione diventa falsa.
# for x in range(6):
for x in range(2, 30, 3):
  print(x)

else:
  print("Finally finished!\n")

# for each
for x in "banana":
  print(x)

else:
  print("Finally finished!\n")
