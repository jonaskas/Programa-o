"""
List - functions
"""

def my_avg(myList):
    sum = 0
    for grade in myList:
        sum += grade
    return sum / len(myList)

def list_one_by_one_v2(myList):
    for item in myList:
        print(item)

def list_one_by_one_v1(myList):
    for i in range(len(myList)):
        print(myList[i])

def change_my_list(myList):
    myList.append(10)
    myList = [1, 1, 1, 1]
    print("Grades:", myList)

grades = [10, 8, 4, 17]
print("Grades:", grades)

print()
list_one_by_one_v1(grades)
list_one_by_one_v2(grades)

print()
print("Avg:", my_avg(grades))

print()
change_my_list(grades)
print("Grades:", grades)
