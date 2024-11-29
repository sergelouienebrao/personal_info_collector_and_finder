#create the file name where data will be stored
file_name = "personal_info_collection.txt"

print("Personal Information Collector")

#make a loop to allow multiple entries
while True:
#prompt for user input
    full_name = input("Full name: ")
    while not full_name:
        print("Full name cannot be empty. Please try again.")
        full_name = input("Full name: ")

    while True:
        gender = input("Gender (Male/Female/Other): ")
        if gender in ["Male", "Female", "Other"]:
            break
        else:
            print("Invalid input. Please enter 'Male,' 'Female,' or 'Other'.")

    address = input("Address: ")
    while not address:
        print("Address cannot be empty. Please try again.")
        address = input("Address: ")

    while True:
        try:
           age_input = int(input("Age: "))
           if age_input > 0:
               break
        except:
            print("Invalid input. Please enter a valid age as a positive number.")

    birthday = input("Birthday (MM/DD/YY): ")
    while not birthday:
        print("Birthday cannot be empty. Please try again.")
        birthday = input("Birthday (MM/DD/YY): ")

    while True:
        contact_number = input("Phone number: ")
        if len(contact_number) == 11:  
         break  
        else:
          print("Invalid input. Please enter a valid phone number that is exactly 11 digits.")

#save the info into the file
    with open(file_name, "a") as file:
        file.write(f"Full name: {full_name}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Age: {age_input}\n")
        file.write(f"Birthday: {birthday}\n")
        file.write(f"Contact Number: {contact_number}\n")
        file.write("\n")

    print("Information saved successfully!")
#ask user if theres another input
    another_input = input("Do you want to add another person? (yes/no): ")
    if another_input != "yes":
      print("Input finished, thank you!")
      break
