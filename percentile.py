n = float(input("Enter the percentage of the student: "))  # Accepts student's percentage as float
if(n > 90):  # If the entered percentage is greater than 90
    print("Grade A")  # Prints Grade A
elif(n > 80):  # If the entered percentage is greater than 80
    print("Grade B")  # Prints Grade B
elif(n > 70):  # If the entered percentage is greater than 70
    print("Grade C")  # Prints Grade C
elif(n >= 60):  # If the entered percentage is 60 or above
    print("Grade D")  # Prints Grade D
else:  # If the entered percentage is below 60
    print("Grade E")  # Prints Grade E