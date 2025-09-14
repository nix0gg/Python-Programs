def largestNum(list1):
    length = len(list1)
    num = 0
    for i in range(length):
        if(i == 0 or list1[i] > num):
            num = list1[i]
        return num
list1 = [1,2,3,4,5,6,7,8,9]
max_num = largestNum(list1)
print("The elements of the list", list1)
print("\nTHe largest number of the list:', max_num")
