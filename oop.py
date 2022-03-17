class Person:
	somePublicProp = 32

	# Costruttore; il primo parametro deve essere il self (this in C++)
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("Davide", 23)

print(p1.name)
print(p1.age)

# Per cancellare l'oggetto p1
del p1

class Student(Person):
	def __init__(self, name, age, id):
		super().__init__(name, age)
		self.id = id

s1 = Student("Davide", 23, 1000)
print(s1.name, s1.age, s1.id, s1.somePublicProp)

# iterator definito in una classe
class MyNumbers:
	# Costruttore dell'iteratore (all'inizio del for)
  def __iter__(self):
    self.a = 1
    return self

	# Ad ogni passata del for
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x

    else:
			# raise serve a scatenare un eccezione
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
