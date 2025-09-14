def converToTitle(string):
    titleString = string.title()
    print("The input string in title case is:", titleString)
userInput = input("Write a sentece:")
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1
if(userInput.istitle()):
    print("The String is already in title case.")
elif(totalSpace > 0):
    converToTitle(userInput)
else:
    print("The String is of one word only")