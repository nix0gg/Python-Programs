smallest = 0
largest = 0
for a in range(0,5):
    x= int(input("Enter number: "))
    if a == 0:
        smallest = largest = x
        if(x < smallest):
            smallest = x
        if(x > largest):
            largest = x
print("Smallest number is:", smallest)
print("Largest number is:", largest)