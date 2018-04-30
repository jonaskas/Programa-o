"""
Exercicio 1
"""
import random

def list_one_by_one_v1(myList):
    for i in range(len(myList)):
        print(myList[i],end=" ")
        

def list_one_by_one_v2(myList):
    for item in myList:
        print(item,end=" ")

grades = random.sample(range(0, 100), 20)

list_one_by_one_v1(grades)
print('\n')
list_one_by_one_v2(grades)
