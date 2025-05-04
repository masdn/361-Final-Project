#Miles Nordwall
#Quad Heap


'''
heapify4 <- arr: , n: heap size, i: element of interest

heapify4 is very similar to heapify using a normal heap
except now 4 children are indexed from the array. This
implemenation of heapify takes advantage of the array-based
indexing strategy by doing a d*i + x calculation, d being
the degree of the tree and x being which of the children to
select.
'''
def heapify4(arr, n , i):
    largest = i
    left = 4 * i + 1
    left_mid = 4*i + 2
    right_mid = 4*i + 3
    right = 4 * i + 4

    #compare i to all its children, keep track of the largest
    #value
    if left < n and arr[left] > arr[largest]:
        largest = left
    if left_mid<n and arr[left_mid] > arr[largest]:
       largest = left_mid
    if right_mid<n and arr[right_mid] > arr[largest]:
       largest = right_mid 
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify4(arr, n, largest)

'''
heapSort <- arr: array to be sorted

This implementation of heap sort is the same as that for
a normal heap but the build heap part starts from floor(n/4)
since we are building a quad heap. 
'''

def heap_sort(arr):
    n = len(arr)
    
    #build the heap startnig from floor(n/4) to 0
    for i in range(n // 4 - 1,-1,-1):
        heapify4(arr, n, i)

    #sort the array using the heap
    for j in range(n - 1, 0, -1):
        #swap the largest value with the jth
        arr[j], arr[0] = arr[0], arr[j]
        #restore the heap property
        #this time on a reduced heap
        #excluding the swapped element (arr[j])
        heapify4(arr, j, 0)



def printArr(arr):
    for i in arr:
        print(i, end= " ")
    print()



    
        


	
