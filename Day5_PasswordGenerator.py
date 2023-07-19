#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_letters = ""
easy_numbers = ""
easy_symbols = ""

for i in range(0, nr_letters):
    easy_letters += random.choice(letters)
for i in range(0, nr_numbers):
    easy_numbers += random.choice(numbers)
for i in range(0, nr_symbols):
    easy_symbols += random.choice(symbols)

easy_pw = easy_letters + easy_symbols + easy_numbers

#Final Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pw = ""
easy_list = []
pw_len = len(easy_pw)
for i in range(0, pw_len):
    easy_list.append(easy_pw[i])

while (easy_list != []):
    new_char_index = random.randint(0, len(easy_list) - 1)
    hard_pw += easy_list[new_char_index]
    easy_list.pop(new_char_index)

print("Generated Password: " + hard_pw)