def sum(numbers):
    if not numbers:
        return 0
    print("Calling sum (%s)" % numbers[1:])  # print out to steps
    remaining_sum = sum(numbers[1:])
    print("Call to sum(%s) returning %d + %d" % (numbers , numbers[0], remaining_sum))  # print out the steps
    return  numbers[0] + remaining_sum

print(sum([1,3,5,2]))

