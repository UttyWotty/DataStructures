from heapq import merge
from re import split

import alist


def merge_sort(list):
    """
    Sorts a list in an Ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sub lists
    Conquer: Recursively sort the sub lists created into previous step
    Combine: Merge the sorted sub lists created in previous step

    Takes O(n log n) 
    """
    if len(list) <= 1:   # if list only has 1 value or less, go back to list- it is done
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """Divide the unsorted list at midpoint into sub lists
    Return the sublist as left and the right
    Runs is logarithmic time O(log n)
    """

    mid = len(list) // 2  # when devide to 2, doesnt allow float number
    left = list[:mid]  # beginning until the midpoint is called left
    right = list[mid:]  #from midpoint to endpoint is called right

    return left, right

def merge(left,right):
    """Merges two lists or arrays sorting them in the process
    returns a new merges list
    O(n log n) runs in overall linear time , it takes n time of merge steps
    """
    l = []
    i = 0  # indexes on left
    j = 0  #indexes on right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n ==1:
        return True
    return list[0] <list[1] and verify_sorted(list[1:])

alist = [54,26,62,93,17,77,31,69]
l = merge_sort(alist)
print(verify_sorted(alist))   # it will check if it the list is sorted
print(l)
print(verify_sorted(l))


