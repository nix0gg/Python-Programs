userInput = input("Write a sentence: ")  # Accepts a sentence from user
totalChar = len(userInput)  # Calculates total characters in the  given sentence
print("Total characters:", totalChar)  # Prints total characters in the given sentence
totalAlpha = totalDigit = totalSpecial = 0  # Initializes counter variables
for a in userInput:  # Loops through each character from the given sentence
    if a.isalpha():  # If the character is an alphabet
        totalAlpha += 1  # Increments the alphabet counter
    elif a.isdigit():  # If the character is a digit
        totalDigit += 1  # Increments the digit counter
    else:  # If the character is a special character
        totalSpecial += 1  # Increments the special character counter
print("Total Alphabets:", totalAlpha)  # Prints total alphabets in the given sentence
print("Total Digits:", totalDigit)  # Print total digits in the given sentence
print("Total Special Characters:", totalSpecial)  # Prints the total special characters in the given sentence
totalSpace = 0  # Initializes space counter
for b in userInput:  # Loops through each character
    if b.isspace():  # If character is a whitespace
        totalSpace += 1  # Increments the space counter
print("Total Spaces:", totalSpace)  # Prints total whitespaces in the given sentence