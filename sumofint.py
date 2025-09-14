sum = 0  # Initialize sum variable
n = int(input("Enter the number:"))  # Accepts a number from user
while n > 0:  # Loops until n becomes 0
    digit = n % 10  # Gets the last digit of the given number
    sum = sum + digit  # Adds digit to sum
    n = n // 10  # Removes the last digit from n
print("The sum of digits of the number is:", sum)  # Print the sum after loop