# new_list = [1, 2, 3]
# result = new_list[0]
# print(result)
#
"""
Search in arrays can be done in 2 ways, if operator or for operator ( manually)
This is linear search because binary search can only be done with sorted lists and sorting takes more space and time
Arrays are not very good for insert and delete methods because both run in linear time
They are good for accessing and reading values
"""
#
# if 1 in new_list: print(True)  #1 listedeyse true de
#
# for n in new_list:   # eger 1 listeyese, true yazdir
#     if n == 1:
#         print(True)
#     break


"""Inserting an array on python.
    When we insert a new value, it resizes not one by one but 0,4,8,16,25,35 etc. So it doesnt have to call resize every
     single time 
    1. Insert method = inserts on index 0, all other values moves more forward.Linear time. Cost runtime
    2. Append method = Inserts on the end of the list. constant time . Doesnt cost extra run time.
    3. Extend method = Inserts a list to another list O(k) k means the number of values we are adding to list
    """

numbers = []  # bosl iste
numbers.insert(1, 2)  # listeye bastan ekledi, ilk sorudugu indexdeki karakter ne
numbers.append(3)  #listeye sondan 1 tane ekledi
numbers.extend([3,4,5,6])  # listeye sondan ekledi
print(numbers)

"""
Delete Operation 
1. Delete operation - deletes the value at index 0 , O(n) linear run time 
"""








