def swap(a,b):  # Defines a function to swap two numbers based on condition
    if(a<b):  # If the first number is less than second
        return b,a  # Swaps and returns the numbers
    else:  # Otherwise
        return a,b  # Returns as is without swapping
num1 = int(input("Enter Number 1: "))  # Accepts first number from user
num2 = int(input("Enter Number 2: "))  # Accepts second number from user
print("Entered values are: ")  # Displays entered values
print("Number 1:", num1)  # Prints first number
print("Number 2:", num2)  # Prints second number
print("Returned value from swap function:")  # Indicates the swap result
num1, num2 = swap(num1,num2)  # Calls swap function and updates the values
print("Number 1:", num1, "Number 2:", num2)  # Prints swapped values