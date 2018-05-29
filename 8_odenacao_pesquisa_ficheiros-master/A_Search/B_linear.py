"""
Linear Search
"""

def search(inlist, item):
    """
    Returns item position on list, -1 otherwise 
    """
    for i in range(len(inlist)):
        if item == inlist[i]:
            return i
    return -1

if __name__ == "__main__":

    search_item  = 6
    my_list = [1, 2, 3, 4, 5, 6, 7]

    position = search(my_list, search_item)

    if position != -1:
        print("item {} is in position: {}".format(search_item, position))
    else:
        print("item {} is not in the list".format(search_item))

