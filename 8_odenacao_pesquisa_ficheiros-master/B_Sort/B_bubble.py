"""
Bubble Sort
"""

import random

def sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(my_list)
    
    print(my_list)
    
    sort(my_list)
    
    print(my_list)
