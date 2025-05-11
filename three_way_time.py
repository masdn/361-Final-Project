import sys 
import numpy as np 
import time
sys.setrecursionlimit(10_000)


# Given 3 sorted arrays (the result of splitting our array into three in threeWay)
# merge them into one by performing 

def merge3Arrs(left, middle,right):
    result = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right):
        # builds list of values and their sources for comparison
        values = []
        if i < len(left):
            values.append((left[i], 'left'))
        if j < len(middle):
            values.append((middle[j], 'middle'))
        if k < len(right):
            values.append((right[k], 'right'))

        if not values:
            break
        
        # vals = [(10, 'l'), (2, 'm'), (5, 'r')] -> smallest = 2, source = left
        smallest, source = min(values, key=lambda x: x[0])

        # grab tuple with the smallest value, append to result from respective list, 
        # increment respective pointer
        if source == 'left':
            result.append(left[i])
            i += 1
        elif source == 'middle':
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1

    return result

def threeWay(arr):
    if (len(arr) <= 1):
        return arr 
    elif len(arr) == 2:
        return arr if arr[0] <= arr[1] else [arr[1], arr[0]]
    # isn't recursion in python fun

    divPoint = len(arr) // 3
    mp1 = divPoint 
    mp2 = divPoint*2

    l = threeWay(arr[:mp1]) # grab beginning to mp1
    m = threeWay(arr[mp1:mp2]) # slice from mp1 to mp2
    r = threeWay(arr[mp2:]) # array from second "midpoint" to end

    return merge3Arrs(l,m,r)



if __name__ == "__main__":
    file = sys.argv[1]
    arr = np.load(file)
    start = time.time() 
    sortedArr = threeWay(arr.tolist())
    end = time.time()
    timeF = end - start
    print("Sorted {file} in {timeF} seconds.\n", file, timeF)
    print(np.array(sortedArr))