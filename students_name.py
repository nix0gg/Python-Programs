name = tuple()  # Initializes an empty tuple to store names of the students
n = int(input("How many names do you want to enter? :"))  # Accepts number of names from the user
for i in range(0, n):  # Loops for each name
    num = input("> ")  # Accepts names from the user
    name = name + (num,)  # Adds names to the tuple
print("\nThe names entered in the tuple are :")  # Prints this statement stating that names are being printed
print(name)  # Prints tuple of names
search = input("\nEnter the name of the student you want to search: ")  # Accepts a name entered by the user to search
if search in name:  # Checks if the entered name is present in the tuple
    print("The name", search, "is present in the tuple")  # Print if the name of the student is found in the tuple
else:  # If the name is not found
    print("The name", search, "is not present in the tuple")  # Prints if the entered name is not found in the tuple
            