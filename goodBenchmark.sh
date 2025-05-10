#!/bin/bash 


# IF YOU ONLY WANT TO TEST 29 AND 30, JUST CHANGE THE FOR LOOP TO 29..30
for i in {20..29}; do
    file="intarrays/array_$i.npy" # NAMED BY MY OTHER SHELL SCRIPT. TO TEST YOUR CODE WITH FLOATS, SIMPLY CHANGE intarrays/ TO floatarrays/
    echo "sorting $file"
    python3 three_way_time.py "$file" # IF YOU WANT TO TEST YOUR CODE, REPLACE MY FILENAME (three_way_time.py) WITH YOURS 
done 