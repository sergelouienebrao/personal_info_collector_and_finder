file_name = "personal_info_collection.txt"
#ask user for the name to search
while True:
    name_search = input("Enter the name to search: ")
    found = False
#open the file
    with open(file_name, "r") as file:
        entries = file.read().strip("-----\n")
        for entry in entries:
            if f"Full Name: {name_search}" in entry:
              print("\nInformation Found:")
              print(entry.strip())
              found = True
              break
    if not found:
        print(f"No information found for '{name_search}'.")

#ask user for another search

