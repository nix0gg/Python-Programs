def discriminant(a, b, c):  # A User Defined Function to calculate discriminant
    d = b**2 - 4*a*c  # Calculates discriminant value
    return d  # Returns discriminant
print("For a quadratic equation in the form of ax^2 + bx + c = 0")  # Prints equation format
a = int(input("Enter the value of a: "))  # Accepts value of a from user
b = int(input("Enter the value of b: "))  # Accepts value of b from user
c = int(input("Enter the value of c: "))  # Accepts value of c from user
det = discriminant(a, b, c)  # Calculates discriminant using function
if(det > 0):  # If the discriminant is positive
    print("The quadratic equation has two real roots.")  # Prints this statement if there are two real roots in the quadratic equation
elif(det == 0):  # If the discriminant is zero
    print("The quadratic equation has one real root.")  # Prints this statement if there is only one real root in the quadratic equation
else:  # If the discriminant is negative
    print("The quadratic equation doesn't have any real roots.")  # Prints this statement if there are no real roots in the quadratic equation
    
