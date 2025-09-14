no_of_std = int(input("Enter number of students:"))
result ={}
for i in range(no_of_std):
    print("Enter details of student No.",i+1)
    roll_no = int(input("Enter roll number:"))
    std_name = input("Enter student name:")
    marks = int(input("Marks:"))
    result[roll_no] = [std_name,marks]
    print(result)
for student in result:
    if result[student][1] > 75:
        print("Student's name who gets more tahn 75 marks is/are:",(result[student][0]))
    