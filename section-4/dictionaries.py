# like objects in JS
# keys must be unique, otherwise only the most recent is taken in account
dogs = {'Fido': 8, 'Sara': 12, 'Matt': 23}

print(dogs)

del(dogs['Sara'])

print(dogs)
print(f'the dictionary length is {len(dogs)}')