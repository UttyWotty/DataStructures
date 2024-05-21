def linear_search(list, target):
    """
    Returns the index  position of the target it found, else returns None
    """
    for i in range(0 , len(list)): # len(list) is a constant time operation
        if list[i] == target:
            return i
    return None

"""
this is linear search so I will check every number from 0 to end of the line until finding the target)

"""
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found on the list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)