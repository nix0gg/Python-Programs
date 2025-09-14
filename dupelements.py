def removeDup(list1):  # Defines function to remove duplicates from a list
    length = len(list1)  # Accepts length of the list
    newlist = []  # Initialize new list for unique elements
    for a in range(length):  # Loops through each element
        if list1[a] not in newlist:  # If the element is not already in newlist
            newlist.append(list1[a])  # Adds the element to newlist
    return newlist  # Returns list without duplicates
list1 = []  # Initializes empty list
inp = int(input("How many elements do you want to add? : "))  # Accepts number of elements from user
for i in range(inp):  # Loops to accept each element
    a = int(input("Enter the elements:"))  # Accepts element from user
    list1.append(a)  # Adds the element to list
print("The list entered is:", list1)  # Prints the entered list
print("The list without any duplicate elements is:", removeDup(list1))  # Prints list without duplicates