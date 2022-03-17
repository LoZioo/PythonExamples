thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
print(thisdict.get("brand"))

# Cancellare un campo

del thisdict["model"]
print(thisdict)

# Ricavare coppia chiave/valore
for x, y in thisdict.items():
  print(x, y)


