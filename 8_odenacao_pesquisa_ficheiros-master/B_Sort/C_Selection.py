"""
Selection Sort
"""

import random

def sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[min_index], my_list[i] = my_list[i], my_list[min_index] # swap

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(my_list)
    
    print(my_list)
    
    sort(my_list)
    
    print(my_list)
