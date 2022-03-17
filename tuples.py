# A differenza delle liste, le tuple sono immutabili e possono solo essere
# concatenate tra di loro; non ci sono operazioni di inserimento, modifica o
# cancellazione previste nella classe di gestione delle tuple.

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Add a list of values the "tropic" variable:
# green -> apple
# tropic -> ['mango', 'papaya', 'pineapple']
# red -> cherry
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Raddoppia gli elementi nella tupla:
# ("apple", "banana", "cherry") diventa:
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
