file_name = "personal_info_collection.txt"
#ask user for the name to search
while True:
    name_search = input("Enter the name to search: ").strip()
    found = False
#open the file
    with open(file_name, "r") as file:
        entries = file.read().split("-----\n")
        
        for entry in entries:
            if f"Full name: {name_search}" in entry:
              print("\nInformation Found:")
              print(entry.strip())
              found = True
              break
    
    if not found:
        print(f"No information found for '{name_search}'.")

#ask user for another search 
    another = input("Do you want to search another person? (yes/no): ")
    if another != "yes":
        print("Search finished, thank you!")
        break
 

 