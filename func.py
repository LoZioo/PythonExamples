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
