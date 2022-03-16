# Sintassi più compatta per assegnare più valori a più variabili
from json import JSONEncoder


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z + '\n')

# Lo si può fare anche con un array come LValue
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z + '\n')

# Il JSON è chiamato dizionario, ma le chiavi devono essere stringhe:
json = {
	"nome":			"Davide",
	"cognome":	"Scalisi"
}

print(json)
print("Nome: %s\n" % json.get("nome"))

# Per quanto riguarda lo scope, si può dichiarare anche una variabile globale
# dentro uno scope diverso da quello globale tramite la parola chiave global:
def myfunc():
  global x	#Variabile globale.
  x = "fantastic"

myfunc()	#Creo la variabile globale.
print("Python is " + x)
