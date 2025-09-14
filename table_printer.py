num = int(input("Enter the number: "))  # Accepts number from user
count = 1  # Initializes counter for multiplication table
while count <= 10:  # Loops to print table from 1 to 10
    prd = num * count  # Calculates product
    print(num, "x", count, "=", prd)  # Prints table line
    count += 1  # Increments the  counter
