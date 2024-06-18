import os
from random import sample
os.system('cls')
import random
number="0123456789"
l_characters="abcdefghijklmnopqrstuvwxyz"
U_characters="ABCDEFGHIJKLMNOPQRSTUVVWXYZ"
special_characters="~`!@#$%^&*()_-+[]:;<=>?/.,''"

all=number+l_characters+U_characters+special_characters
ent=int(input("Enter The length for the password:"))
length=ent
password="".join(random.sample(all,length))
print("Your Password is Generated:",password)
