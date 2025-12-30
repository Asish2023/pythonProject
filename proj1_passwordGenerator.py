import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
        '{', '}', '[', ']', '|', '', ':', ';', '"', '<', '>', ',', '.', '?', '/', '~',
        '`',"'"]

print("Welcome to Password Generator!\n")

print("-------------------------------------")
n_letters = int(input("How many letters: "))
print("-------------------------------------")
n_numbers = int(input("How many numbers: "))
print("-------------------------------------")
n_special_chars = int(input("How many special characters: "))
print("-------------------------------------\n")

pass_list = []

for i in range(n_letters):
        pass_list.append(random.choice(letters))

for i in range(n_numbers):
        pass_list.append(random.choice(numbers))  

for i in range(n_special_chars):
        pass_list.append(random.choice(special_chars))

random.shuffle(pass_list)
password = ''.join(pass_list)

print("Your password is: " + password)
print("\n-------------------------------------\n")


