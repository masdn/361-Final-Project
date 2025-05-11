#Ayman Hassen
#Random Quicksort
import sys 
import time
import numpy as np

import random
'''
rand_QS <- arr: array to be sorted
arr: array to be sorted
low: lower bound of the array
high: upper bound of the array
p: pivot element
QS: acts as a helper function that recursively sorts the low and high
partitions that come from p. 
'''
def rand_QS(arr):
    def QS(arr, low, high):
        if low < high:
            p = partition (arr, low, high)
            QS(arr, low, p-1)
            QS(arr, p+1, high)

    copy_Arr = list(arr)
    QS(copy_Arr, 0, len(copy_Arr)-1)
    return copy_Arr
'''
partition <- arr: array to be sorted
The partition function uses Lomuto partitioning which begins with choosing a random index within the bounds of the
current subarray swaping the particular element with the last element used in p.
'''
def partition(arr, low, high):
    pIndex = random.randint(low, high)
    arr[pIndex], arr[high] = arr[high], arr[pIndex]
    p = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

if __name__ == "__main__":
    file = sys.argv[1]
    arr = np.load(file)
    start = time.time() 
    sortedArr = rand_QS(arr.tolist())
    end = time.time()
    timeF = end - start
    print("Sorted {file} in {timeF} seconds.\n", file, timeF)
    print(np.array(sortedArr))