import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("wellcome to password generator!")
size = int (input ("size of the password : "))
nr_letters =int(input("how many letters would you like in your password? : ")) 
nr_symbols = int(input("how many symbols would you like in your password? : "))
nr_numbers = int(input("how many numbers would youlike in your password? : "))

password_list = []


for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
    
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    
print(f"your random generated password is : {password}")