num1 = float(input("Enter first number: "))  # Accepts first number from user
num2 = float(input("Enter second number: "))  # Accepts second number from user
num3 = float(input("Enter third number: "))  # Accepts third number from user
if (num1 >= num2) and (num1 >= num3):  # Checks if num1 is largest
    largest = num1  # Assigns num1 as largest
elif (num2 >= num1) and (num2 >= num3):  # Checks if num2 is largest
    largest = num2  # Assigns num2 as largest
else:  # Otherwise, num3 is largest
    largest = num3  # Assigns num3 as largest
print("The largest number is", largest)  # Prints the largest number