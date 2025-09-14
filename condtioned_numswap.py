def swap(a,b):
    if(a<b):
        return b,a
    else:
        return a,b
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
print("Entered values are: ")
print("Number 1:", num1)
print("Number 2:", num2)
print("Returned value from swap function:")
num1, num2 = swap(num1,num2)
print("Number 1:", num1, "Number 2:", num2)