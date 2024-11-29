#create the file name where data will be stored
file_name = "personal_info_collection.txt"

#make a loop to allow multiple entries
while True:
#prompt for user inputs

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
        file.write("\n")
#ask user if theres another input
    another_input = input("Do you want to add another person? (yes/no): ")
    if another_input != "yes":
      print("Input finished, thank you!")
      break
