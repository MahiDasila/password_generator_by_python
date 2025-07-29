import random
print("***PASSWORD GENERATOR***")
letter_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','L','M','N','N','O','P','Q','R','S','T','U','V','X','Y','Z']
letters=int(input("enter how many letter you want to print: \n"))
symbol_list =symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '[', ']', '{', '}', ':', ';', '"', '<', ',', '.', '>', '/', '?', '|', '\\']
symbols= int(input("enter how many symbols you want to add: \n"))
number_list  =['1','2','3','4','5','6','7','8','9','0']
numbers= int(input("enter how many numbers you want to add: \n"))
password_list=[]
for i in range(1 , letters+1):
  password_list.append(random.choice(symbol_list))
for i in range(1 , symbols+1):
 password_list.append(random.choice(symbol_list))
for i in range(1 , numbers+1):
 password_list.append(random.choice(symbol_list))
random.shuffle(password_list)
assword = ''.join(password_list)
print("Generated Password:", password_list)