def largestNum(list1):  # Defines function to find largest number in list
    length = len(list1)  # Accepts length of the list
    num = 0  # Initializes variable to store largest number
    for i in range(length):  # Loops through each element
        if(i == 0 or list1[i] > num):  # If the first element or current element is greater than num
            num = list1[i]  # Updates num with current element
    return num  # Returns the largest number
list1 = [1,2,3,4,5,6,7,8,9]  # Defines a list of numbers
max_num = largestNum(list1)  # Finds the largest number in the list
print("The elements of the list", list1)  # Prints the list
print("\nThe largest number of the list:", max_num)  # Prints the largest number
