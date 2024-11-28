#create the file name where data will be stored

#make a loop to allow multiple entries
while True:
    try: 
        full_name = input("Full name: ")
        address = input("Address: ")
        age = int(input("Age: "))
        birthday = int(input("Birthday (MM/DD/YY): "))
        contact_number = int(input("Phone number: "))

    except:
        print("Invalid input, try again.")
    break

print(full_name)
print(age)
print(birthday)
print(contact_number)

 
#prompt for user inputs

#save the info into the file 

#ask if theres another input