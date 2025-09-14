row = int(input("Enter the number of rows:"))  # Accepts the number of rows from user
for i in range(row, 0, -1):  # Loops from row down to 1
    for j in range(1, i+1):  # Loops from 1 up to i
        print(j, end="")  # Prints numbers on the same line
    print()  # Moves to next line after each row
