print("QUESTION 4")
# a
dict = {1: 0}
for i in range(2, 31):
    dict[i] = (i-1) * i
print(dict)

# b

for key, value in dict.items():
    print(key, ":", value)

# c
sum = 0
for value in dict.values():
    sum += value
print("Sum of values in dict_a:", sum)

# d
user_input = int(input("Enter a number between 1 and 30 to remove its key-value pair: "))
if user_input in dict:
    del dict[user_input]
    print("Key-value pair removed.")
else:
    print("Invalid input. Key not found in dictionary.")
