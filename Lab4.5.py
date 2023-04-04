print("QUESTION 5")
# a
divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {**divided, **we_fall}
print("Name\tAge")
for name, age in united_we_stand.items():
    print(name, "\t", age)

#  b
del united_we_stand['Nat']
print("\nAfter removing 'Nat':")
print("Name\tAge")
for name, age in united_we_stand.items():
    print(name, "\t", age)

# c
print("\nSorted by key:")
print("Name\tAge")
for name, age in sorted(united_we_stand.items()):
    print(name, "\t", age)

#  d
print("\nMax age:", max(united_we_stand.values()))
print("Min age:", min(united_we_stand.values()))
