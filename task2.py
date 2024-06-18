import os 
os.system('cls')
import math

tasks=[]
# print(tasks)
def menu():
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Multiplication\n")
    print("4. Division\n")
    print("5. Modulus\n")
    print("6. Exponent\n")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        add()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==2:
        sub()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==3:
        mul()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==4:
        div()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==5:
        mod()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
    
    if choice==6:
        expo()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    else:
        exit()
    
    
        
def add():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    print("Additon:-",num1+num2)

def sub():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    print("Subtraction:-",num1-num2)
    
def mul():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    print("Multiplication:-",num1*num2)
    
def div():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    print("Division:-",num1/num2)
    
def mod():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    print("Modulus:-",num1%num2)
    
def expo():
    num1=int(input("Enter the number:-"))
    num2=int(input("Enter the power:-"))   
    print("Exponent:-",num1**num2)
    
menu()