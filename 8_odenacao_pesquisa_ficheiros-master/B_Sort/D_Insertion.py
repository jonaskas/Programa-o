"""
insertion Sort
"""

import random

def sort(my_list):
    for index in range(1, len(my_list)):
        currentvalue = my_list[index]
        position = index
        while position > 0 and my_list[position-1] > currentvalue:
            my_list[position] = my_list[position - 1]
            position -= 1
        my_list[position] = currentvalue

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(my_list)
    
    print(my_list)
    
    sort(my_list)
    
    print(my_list)
