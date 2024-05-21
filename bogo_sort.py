import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

print(numbers)

def is_sorted(values):
    for index in range(len(values) - 1):  # her value sorting yaptiginda listeden dus
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    """
    Bogo sort is to sort the numbers/names in a list everytime randomly
     """
    attempts = 0  # saymaya sifirdan basliyoruz
    while not is_sorted(values):
        print(attempts) # her denemeyi ekrana yazdir
        random.shuffle(values)
        attempts += 1  # her denemede 1 artiyor
    return values  #listedeki degerleri dondur

print(bogo_sort(numbers))   #toplam kac defada cozdugunu gosteriyor



