import random

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 10
nr_symbols = 10
nr_numbers = 10
chosen_letters = []
chosen_symbols = []
chosen_numbers = []
for ltrs in range(1, nr_letters + 1):
    chosen_letters.append(random.choice(letters))

for smbs in range(1, nr_symbols +1):
    chosen_symbols += random.choice(symbols) #Substitui a função .append

for nbrs in range(1, nr_numbers + 1):
    chosen_numbers += random.choice(numbers)

final_password = chosen_letters + chosen_symbols + chosen_numbers
gen_password = list(final_password)
random.shuffle(gen_password)
gen_password = gen_password[:18]
final_password = "".join(gen_password)

print(final_password)
print(len(final_password))