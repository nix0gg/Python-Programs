n = int(input("Enter a number:"))  # Accepts number from user
temp = n  # Stores original number for comparison
reverse = 0  # Initializes variable to store reversed number
while(n > 0):  # Loops until n becomes 0
    digit = n % 10  # Gets the last digit from the number
    reverse = reverse * 10 + digit  # Builds a reversed number
    n = n // 10  # Removes last digit from n
if(temp == reverse):  # Checks if original and reversed numbers are equal
    print("Palindrome")  # Prints if the given number is palindrome
else:  # If not equal
    print("Not palindrome")  # Prints if the given number is not palindrome
