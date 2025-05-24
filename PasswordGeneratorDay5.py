'''
import random
print("Welcome to pypassword generator!")
letter = int(input("How many letters would you like in your password?"))
symbol = int(input("How many symbols would you like?"))
number = int(input("How many numbers would you like?"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

password = ""
for let in range(letter):
    password += random.choice(letters)
for let in range(symbol):
    password += random.choice(symbols)
for let in range(number):
    password += str(random.choice(numbers))
print(password)
'''

# To find max value with different ways
list1 = [11, 6, 3, 4, 5, 2]
# Option1
print(max(list1))

# Option2
list1 = sorted(list1)
print(list1[-1])

# Option3
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)
