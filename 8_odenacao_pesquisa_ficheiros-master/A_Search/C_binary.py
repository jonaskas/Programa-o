"""
Binary Search
"""

from math import ceil

def search(inlist, item):
    """
    Returns item position on list, -1 otherwise 
    """
    start = 0
    end = len(inlist) - 1
    while start <= end:
        mid = ceil((start + end) / 2)
        if inlist[mid] == item:
            return mid
        if inlist[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1

if __name__ == "__main__":

    search_item  = 6
    my_list = [1, 2, 3, 4, 5, 6, 7]

    position = search(my_list, search_item)

    if position != -1:
        print("item {} is in position: {}".format(search_item, position))
    else:
        print("item {} is not in the list".format(search_item))

