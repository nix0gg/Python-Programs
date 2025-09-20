no_of_std = int(input("Enter number of students:"))  # Accepts number of students from user
result = {}  # Initializes empty dictionary to store student details
for i in range(no_of_std):  # Loops for each student
    print("Enter details of student No.", i+1)  # Prints a statement to enter details
    roll_no = int(input("Enter roll number:"))  # Accepts roll number
    std_name = input("Enter student name:")  # Accepts student name
    marks = int(input("Marks:"))  # Accepts marks
    result[roll_no] = [std_name, marks]  # Stores details in dictionary
print(result)  # Prints current state of dictionary
for student in result:  # Loops through dictionary to check marks
    if result[student][1] > 75:  # A condition if the marks are greater than 75
        print("Student's name who Acceptss more than 75 marks is/are:", (result[student][0]))  # Prints student name
    