# Verifica di appartenenza
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Foreach con item
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Foreach con indice
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# List Comprehension
# Leggere questa sintassi facendo un analogia alla scrittura matematica o ad SQL

# You want a new list, containing only the fruits with the letter "a" in the name
# I seguenti due algoritmi sono equivalenti:
# 1)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# [(SQL SELECT) expression (SQL FROM) for item in iterable (SQL WHERE) if condition == True]
# The return value is a new list, leaving the old list unchanged.
# 2)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if "a" in x]
print(newlist)

# In expression può anche esserci una condizione:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
