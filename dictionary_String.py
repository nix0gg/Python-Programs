myStr = "2nd PU Course"
print("The input string is:", myStr)
myDict = dict()
for character in myStr:
    if character in myDict:
        myDict[character]+=1
    else:
        myDict[character]+=1
print("The dictionary created from characters of the string is:")
print(myDict)