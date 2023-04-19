phoneDirectory = {}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
print("1.Add a record")
print("2.Search a record")
print("3.Update a record")
print("4.Delete a record")
print("5.Quit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        
        while True: 
          num = input("Enter your 10-digit phone number: ")
          if len(num) == 10 and num.isdigit():
             phoneDirectory[name] = num
             print("Record added")
             break
        
          else:
             print("Invalid phone number. Please enter a 10-digit number.")
    elif choice == 2:
        search = input("Enter name to search: ")
        if search in phoneDirectory:
          print(f"{search}:{phoneDirectory[search]}")
        else:
            print("Number does not exist")
    elif choice ==3:
        Name = input("Enter name: ")
        while True:
          numb = (input("Enter new 10-digit phone number: "))
          if len(numb) == 10 and numb.isdigit():
           phoneDirectory[name]=numb
           print("Record updated")
           break
          else:
           print("Invalid phone number. Please enter a 10-digit number.")
    elif choice ==4:
        remove = input("Enter name: ")
        if remove in phoneDirectory:
            phoneDirectory.pop(remove)
            print("Record deleted")
    elif choice ==5:
        print("Thank you for using GRANN'S PHONE DIRECTORY")
        break
    else:
        print("Choice invalid!")