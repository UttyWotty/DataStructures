# bu kod bize true value yu dondurecek, normal binary indexi dondurmustu

"""
Recursive dedigimiz, normal binary gibi once ortalamayi aliyor, sorna eger ortalamanin uzerindeyse +1 ekliyor,
degilse cikariyor, onemli olan sayiyi bulmak degil, hangi aralikta olsdugunuz bulmak.
Her seferinde returm yapip, bir islem bitince yine en bastan baslatiyor, (kendini kendini cagiriyor)
recursive should have a stop condition, in here, first on is if the list is empty, if yes, code stops.
2nd one is when target is the midpoint of the list
recursive dept = how many times the code called itself 
"""

def recursive_binary_search(list, target):
    if len(list) == 0:  # eger liste bossa, False dondur
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] ==target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1: ], target)
            else:
                return recursive_binary_search(list[ :midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)