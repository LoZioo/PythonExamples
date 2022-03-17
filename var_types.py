# https://www.w3schools.com/python/python_datatypes.asp

# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

z = 3 + 4j
print("z: %f %fj, type(z): %s" % (z.real, z.imag, type(z)))

# set
x = {"apple", "banana", "cherry"}
print(x)

# dict (o json)
x = dict(name="John", age=36)
x = {"name": "John", "age": 36}
print(x)

# tuple (immutabile)
x = ("apple", "banana", "cherry", 123)
print(x)

# list (o array) (mutabile)
x = ["apple", "banana", "cherry", 123]
print(x)
