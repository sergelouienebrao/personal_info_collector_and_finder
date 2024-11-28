#create the file name where data will be stored
file_name = "personal_info_collection.txt"

#make a loop to allow multiple entries
while True:
#prompt for user inputs
    try: 
        full_name = input("Full name: ")
        address = input("Address: ")
        age = int(input("Age: "))
        birthday = (input("Birthday (MM/DD/YY): "))
        contact_number = int(input("Phone number: "))

#save the info into the file
        with open(file_name, "a") as file:
            file.write(f"Full name: {full_name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Birthday: {birthday}\n")
            file.write(f"Contact Number: {contact_number}\n")

    except:
        print("Invalid input, try again.")
    




#ask user if theres another input