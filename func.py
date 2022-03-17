# Default parameters
def my_function(name = "Davide"):
	print("Hello from a function! Name: %s" % name)
	return name

my_function("Lemuel")
my_function("Luigi")
print(my_function())

# I parametri possono essere dati in qualsiasi ordine diverso dal predefinito.
# In questo caso, l'ordine va specificato come segue:
def my_function(child3, child1, child2):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# lambda parameters : expression
x = lambda a, b : a * b
print(x(5, 6))

# Python uses a mechanism, which is known as "Call-by-Object",
# sometimes also called "Call by Object Reference" or "Call by Sharing"

# If you pass immutable arguments like integers, strings or tuples to a function,
# the passing acts like Call-by-value. It's different, if we pass mutable arguments.

# All parameters (arguments) in the Python language are passed by reference.
# It means if you change what a parameter refers to within a function,
# the change also reflects back in the calling function.

student = {
	'Archana':	28,
	'krishna':	25,
	'Ramesh':		32,
	'vineeth':	25
}

def test(student):
   new = {'alok':	30,'Nevadan':	28}

   student.update(new)
   print("Inside the function", student)
   return

test(student)
print("outside the function:", student)

student = {
	'Archana':	28,
	'krishna':	25,
	'Ramesh':		32,
	'vineeth':	25
}

# Nel caso sopra, viene passato PER VALORE, un RIFERIMENTO all'oggetto
# Si può modificare il riferimento all'oggetto senza riflettere le modifiche
# nello scope del chiamante, ma se si aletera l'oggetto tramite i suoi metodi,
# allora i cambiamenti si andranno a riflettere anche nello scope chiamante.

# Se infatti si passa un intero, non si passa un oggetto, ma si passa un tipo "base".
# Se questo viene infatti modificato all'interno della funzione, i cambiamenti non
# si riversano all'esterno dello scope della funzione.

x = 2
def test(x):
   x = 3

   print("Inside the function", x)
   return

test(x)
print("Outside the function:", x)
