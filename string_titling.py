def converToTitle(string):  # Defines a user defined function to convert string to title case
    titleString = string.title()  # Converts string to title case
    print("The input string in title case is:", titleString)  # Prints title case string
userInput = input("Write a sentence:")  # Accepts input string from user
totalSpace = 0  # Initializes space counter
for b in userInput:  # Loops through each character
    if b.isspace():  # If the character is a whitespace
        totalSpace += 1  # Increments the space counter
if(userInput.istitle()):  # Checks if the string is already in title case
    print("The String is already in title case.")  # Prints this message if the string is already in title case
elif(totalSpace > 0):  # If the string contains whitespaces
    converToTitle(userInput)  # Converts the string to title case 
else:  # If the string is a single word
    print("The String is of one word only")  # Prints this message if the string is a single word