def binary_search(list, target):
    first = 0 #first element in the list is 0
    last = len(list)-1 #odan baslamaya baslasigi icin, en yuksek sayi n -1 )
    while first <= last:  # bulunan ilk sayi son sayiya esir ya da kcuuk oldugu surece;
        midpoint = (first+last) //2 # 2 tane yazarsak , ortalamaya en yakin tam sayiya tamamlar

        if list[midpoint] ==target:  # aradigimiz rakam tam orta rakamsa,
            return midpoint  # best case scenario
        elif list[midpoint] < target: # aradigimiz rakam ortanin altindaysa ortalamaya 1 ekle,
            first = midpoint +1
        else:
            last = midpoint -1 # sayi ortanin altindaysa ortalamadan 1 cikar
    return None
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found on the list")

numbers = [1,2,3,4,5,6,7,8,9,10]  # list has to be sorted!!
result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 5)
verify(result)

