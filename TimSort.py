from typing import List
import sys 
import time
import numpy as np

def insertion_sort(arr: List[float], left: int, right: int) -> None:
    """
    Sorts a portion of the array in-place using insertion sort.
    Args:
        arr: The list of numbers to sort.
        left: The starting index of the portion to sort.
        right: The ending index of the portion to sort.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr: List[float], left: int, mid: int, right: int) -> None:
    """
    Merges two sorted subarrays of arr in-place.
    Args:
        arr: The list of numbers to merge.
        left: The starting index of the first subarray.
        mid: The ending index of the first subarray.
        right: The ending index of the second subarray.
    """
    len1, len2 = mid - left + 1, right - mid
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def timsort(arr: List[float], run: int = 32) -> None:
    """
    Sorts the array in-place using the Timsort algorithm.
    Args:
        arr: The list of numbers to sort.
        run: The size of the initial run for insertion sort (default: 32).
    """
    n = len(arr)
    # Sort individual subarrays of size RUN
    for i in range(0, n, run):
        insertion_sort(arr, i, min(i + run - 1, n - 1))
    # Merge subarrays
    size = run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

def main() -> None:
    """Demonstrates the usage of the timsort algorithm with an example array."""
    arr = [5, 21, 7, 23, 19, 10, 1, 3, 2, 8, 6, 4, 11, 15, 13, 12, 9, 14, 16, 18, 17, 20, 22, 24, 25]
    print("Original array:", arr)
    timsort(arr)
    print("Sorted array:  ", arr)

if __name__ == "__main__":
    file = sys.argv[1]
    arr = np.load(file)
    start = time.time() 
    sortedArr = timsort(arr.tolist())
    end = time.time()
    timeF = end - start
    print("Sorted {file} in {timeF} seconds.\n", file, timeF)