import os 
os.system('cls')

tasks=[]
# print(tasks)
def menu():
    print("1. Add task\n")
    print("2. Read task\n")
    print("3. Update task\n")
    print("4. Delete task\n")
    print("5. Search task\n")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        addTask()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==2:
        ReadTask()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==3:
        UpdateTask()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==4:
        removeTask()
        print("y or n\n")
        cont=input("Do you want to Continue\n")
        if cont=='y':
            menu()
        else:
            exit()
            
    if choice==5:
        searchTask()
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
    else:
        exit()
        
        
def addTask():
    task=input("Enter the Task:-")
    tasks.append(task)

    if tasks!=None:
        print("Task Added Successfully")
    else:
        print("Failed to Add Task")

def ReadTask():
    print("\nFetching All The Tasks...\n")
    for t in tasks:
        print(t,"\n")
        
        
def UpdateTask():
    ind=int(input("Enter the task index you want to update:"))
    utask=input("Enter the Task:-")
    tasks[ind]=utask
    if(utask in tasks):
        print("Task Updated Successfully")
    else:
        print("Task Updated Failure")
        
def removeTask():
    ind=int(input("Enter the task index you want to remove:"))
    del tasks[ind]
    ReadTask()

def searchTask():
    ind=int(input("Enter the task index you want to search:"))
    if(tasks[ind] in tasks):
        print("Task Searched is -",tasks[ind])
    else:
        print("There are no/wrong task index to search")
    
menu()