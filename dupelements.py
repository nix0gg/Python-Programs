def removeDup(list1):
    length = len(list1)
    newlist = []
    for a in range(length):
        if list1[a] not in newlist:
            newlist.append(list1[a])
    return newlist
list1=[]
inp=int(input("How many elements do you want to add? : "))
for i in range(inp):
    a = int(input("Enter the elements:"))
    list1.append(a)
print("The list entered is:",list1)
print("The list without any duplicate elements is:",removeDup(list1))