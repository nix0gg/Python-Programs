name = tuple()
n = int(input("How many names do you want to enter? :"))
for i in range(0,n):
    num = input("> ")
    name = name +(num,)
print("\nThe names entered in the tuples are :")
print(name)
search = input("\nEnter the name of the student you want to searcH: ")
if search in name:
    print("The name", name, "is present in the tuple")
else:
    print("The name" , name, "is not present in the tuple")
            