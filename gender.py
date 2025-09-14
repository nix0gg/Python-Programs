def prefix(name, gender):  # Defines function to print greeting based on gender
    if(gender == 'M' or gender == 'm'):  # If gender is male
        print("Hello, Mr.", name)  # Prints greeting for male
    elif(gender == 'F' or gender == 'f'):  # If gender is female
        print("Hello, Ms.", name)  # Prints greeting for female
    else:  # If gender is not M or F
        print("Please enter only M or F in gender")  # Prints error message
name = input("Enter your name:")  # Accepts user's name
gender = input("Enter your gender: M for male, F for female:")  # Accepts user's gender
prefix(name, gender)  # Calls function to print greeting