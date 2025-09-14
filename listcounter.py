list1 = [10, 20, 30, 40, 50, 60, 20, 50, 10, 30, 24, 45]  # Defines a list of numbers
print("The list is:", list1)  # Prints the list
inp = int(input("Which element occurrence would you like to count?"))  # Accepts element to count from user
count = list1.count(inp)  # Counts the occurrences of the element in the list
print("The count of element", inp, "in the list is:", count)  # Prints the count of an occurring element
