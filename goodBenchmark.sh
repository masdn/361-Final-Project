#!/bin/bash 

for i in {20..29}; do
    file="intarrays/array_$i.npy"
    echo "sorting $file"
    python3 three_way_time.py "$file"
done 