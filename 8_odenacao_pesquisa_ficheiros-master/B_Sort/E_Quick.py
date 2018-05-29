"""
Quick Sort
"""

import random

def sort(my_list):

    def qsort(my_list, first, last):
        if first < last:
            in_place = partition_no_print(my_list, first, last)
            # sort left of in_place element
            qsort(my_list, first, in_place-1)
            # sort right of in_place element
            qsort(my_list, in_place+1, last)
    
    def partition_no_print(my_list, first, last):
        pivot = my_list[first]
        left = first + 1
        right = last
        while True:
            while left <= right and my_list[left] <= pivot:
                left += 1
            while right >= left and my_list[right] >= pivot:
                right -= 1
            if left <= right:
                my_list[right], my_list[left] = my_list[left], my_list[right]
            else: 
                break
        # swaps pivot and right, left elements are lower than pivot and right elements are greather tha pivor
        my_list[first], my_list[right] = my_list[right], my_list[first]
        return right

    qsort(my_list, 0, len(my_list)-1)

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(my_list)
    
    print(my_list)
    
    sort(my_list)
    
    print(my_list)
