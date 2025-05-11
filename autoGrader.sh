#!/bin/bash 

files=("three_way_time.py" "TimSort.py" "rand_quicksort.py" "quad_heap.py")
inputs=("graderArrInt.npy" "graderArrFloat.npy")

for file in "${files[@]}"; do
    echo "Sorting using $file"
    for input in "${inputs[@]}"; do
        python3 $file $input 
    done
done
