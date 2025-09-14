smallest = 0  # Initializes variable for smallest number
largest = 0  # Initializes variable for largest number
for a in range(0, 5):  # Loops to accept 5 numbers from user
    x = int(input("Enter number: "))  # Accepts number from user
    if a == 0:  # For the first number
        smallest = largest = x  # Sets both smallest and largest to first number
    if x < smallest:  # If the current number is smaller than smallest
        smallest = x  # Updates the smallest number
    if x > largest:  # If the current number is larger than largest
        largest = x  # Updates the largest number
print("Smallest number is:", smallest)  # Prints smallest number
print("Largest number is:", largest)  # Prints largest number