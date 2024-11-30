file_name = "personal_info_collection.txt"
#ask user for the name to search
while True:
    name_search = input("Enter the name to search: ")
#open the file
    with open(file_name, "r") as file:
        entries = file.read().strip("-----\n")

#search for the name

#ask user for another search
