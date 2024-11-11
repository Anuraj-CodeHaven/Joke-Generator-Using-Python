#Author: Anuraj R 

import random 
print("---- welcome to pass maker ----\n")
character="QWERTYUIOPASDGFHJKLZXCVBNM"
small="qwertyuiopasdfghjklzxcvbnm"
number="1234567890"
special="_!@#₹%^&*':;,?`,."
pass_size=int(input("Enter the number that indicating size of the generating password : "))
allc=character+small+number+special
password=""
while pass_size>0:
    password=password+random.choice(allc)
    pass_size=pass_size-1
print()    
print("\n----you generated password----\n")
print(password)
print("\n")
print("----Thank you for using ----")
