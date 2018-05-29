"""
Merge Sort
"""

import random

def sort(my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        # Split
        sort(left)
        sort(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(my_list)
    
    print(my_list)
    
    sort(my_list)
    
    print(my_list)
