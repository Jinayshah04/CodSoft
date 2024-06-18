import os
os.system('cls')

names=[]
phone_numbers=[]
emails=[]
address=[]

def menu():
    print("1.Add 2.View 3.Find 4.Update 5.Delete 6.Exit\n")
    choice=int(input("Enter Your Choice:\n"))
    if choice==1:
        add()
        print(" y or n")
        cont=input("\nDo You Continue:\n")
    
        if cont=='y':
            menu()
        elif cont=='n':
            exit()
    if choice==2:
        view()
        print(" y or n")
        cont=input("\nDo You Continue:\nw")
    
        if cont=='y':
            menu()
        elif cont=='n':
            exit()
    if choice==3:
        find()
        print(" y or n")
        cont=input("\nDo You Continue:\nw")
    
        if cont=='y':
            menu()
        elif cont=='n':
            exit()

    if choice==4:
        upd()
        print(" y or n")
        cont=input("\nDo You Continue:\nw")
    
        if cont=='y':
            menu()
        elif cont=='n':
            exit()

    if choice==5:
        delete()
        print(" y or n")
        cont=input("\nDo You Continue:\nw")
    
        if cont=='y':
            menu()
        elif cont=='n':
            exit()
    
    else:
        exit()

def add():
    lim=int(input("How Many Elements You Want to Add in your Contact:\n"))

    for i in range(0,lim):
        name = input("Name: ")
        phone_number=int(input("Phone Number: "))
        email = input("Email: ")
        addr = input("Address: ")
        names.append(name)
        phone_numbers.append(phone_number)
        emails.append(email)
        address.append(addr)

        if phone_number>=1000000000 and phone_number<=9999999999:
            print("Added Successfully\n")
        else:
            print("Enter Valid Phone Number\n")
            print(" y or n")
            cont=input("\nDo You Want to Try Once more for Phone Number:")

            if cont=='y':
                add()
            else:
                exit()

def view():
    print(names,phone_numbers,emails,address)

def find():
    search_term = input("\nEnter search term: ")

    print("Search result:")

    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        print("Name: {}, Phone Number: {}".format(search_term, phone_number))

    else:
        print("Name Not Found")

def delete():
    n=int(input("Enter Index of Name:"))
    pn=int(input("\nEnter Index of Phone Number:"))
    if n==pn:
        names.pop(n)
        phone_numbers.pop(pn)
        print(names)
        print(phone_numbers)
    else:
        print("Enter Same Index Number for Name and Phone Number")

        print("y or n")
        cont=input("\nDo you want to try Once:")

        if cont=='y':
            delete()
        else:
            exit()

def upd():
    i=int(input("Enter Index Of that Number Which Contact You want To Update:"))
    phone_number=int(input("Enter Updated Phone Number:"))
    phone_numbers[i]=phone_number
    print(names)
    print(phone_numbers)

menu()