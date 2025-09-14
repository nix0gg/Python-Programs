myStr = "Hello World!"  # Defines the input string
print("The input string is:", myStr)  # Prints the input string
myDict = dict()  # Initializes an empty dictionary
for character in myStr:  # Iterates over each character in the string
    if character in myDict:  # If the character already in dictionary
        myDict[character] += 1  # Increments its count
    else:  # If the character is not in dictionary
        myDict[character] = 1  # Sets its count to 1
print("The dictionary created from characters of the string is:")  # Prints the result message
print(myDict)  # Prints the dictionary with character counts