#Password Generator Project

import random

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

''' Method 1 '''

# # Easy way
# password=""
# for let in range(0,nr_letters):
#     password += random.choice(letters)   #the choice() method returns a randomly selected element from the specified sequence
    
# for sym in range(0,nr_letters):
#     password += random.choice(symbols)
    
# for num in range(0,nr_letters):
#     password +=random.choice(numbers)
    
# print(f"Your password is : {password}.")

# Hard way
password=""
random_password=""
for let in range(0,nr_letters):
    password += random.choice(letters)
    
for sym in range(0,nr_letters):
    password += random.choice(symbols)
    
for num in range(0,nr_letters):
    password +=random.choice(numbers)

for i in password:
    random_password += random.choice(password)

print(f"Your password is : {random_password}.")

# ''' Method 2 for Hard way'''
# password_list=[]
# password=""
# for let in range(0,nr_letters):
#     password_list.append(random.choice(letters)) # we can also use append instead of +=
    
# for sym in range(0,nr_letters):
#     password_list += random.choice(symbols)
    
# for num in range(0,nr_letters):
#     password_list +=random.choice(numbers)

# random.shuffle(password_list)

# for i in password_list:
#     password+=i
    
# print(f"Your Password is : {password}.")
    

    

    
    