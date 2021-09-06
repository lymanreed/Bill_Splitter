# the list "walks" is already defined
# your code here
total = 0
for e in walks:
    total += e['distance']

print(total // len(walks))
