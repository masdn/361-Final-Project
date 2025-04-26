#Miles Nordwall
#Quad Heap

def heapSort(arr):
    n = len(arr)

    for i in range(n // 4 - 1,-1,-1):
        heapify4(arr, n, i)

    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[j], arr[0]
        heapify4(arr, j, 0)

def heapify4(arr, n , i):
    largest = i
    left = 4*i + 1
    left_mid = 4*i + 2
    right_mid = 4*i + 3
    right = 4*i + 4

    if left<n and arr[left] > arr[largest]:
        largest = left
    if left_mid<n and arr[left_mid] > arr[largest]:
        largest = left_mid
    if right_mid<n and arr[right_mid] > arr[largest]:
        largest = right_mid 
    if right<n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify4(arr, n, largest)


def printArr(arr):
    for i in arr:
        print(i, end= " ")
    print()

arr = [9,4,3,8,10,2,5]
heapSort(arr)
printArr(arr)


    
        


	
