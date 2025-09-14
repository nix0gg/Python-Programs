name = input("What is your name? :")  # Accepts user's name
age = int(input("What is your age? :"))  # Accepts user's age and convert to integer
if age >= 18:  # Check if age is 18 or above
    print("You are eligible to apply for a driving license!")  # Eligible for driving license
else:  # If age is less than 18
    print("You are not eligible to apply for a driving license.")  # Not eligible for driving license
