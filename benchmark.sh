#!/bin/bash

ALG1="TimSort.py"
ALG2="3waytime.py"
ALG3="quad_heap.py"
ALG4="rand_quicksort.py"

RESULTS_FILE="benchmark_results.txt"
echo "Benchmarking results" > "$RESULTS_FILE"

# Array of data sizes from 2^20 to 2^30
for ((n=20; n<=30; n++)); do
    SIZE=$((2 ** n))
    echo "Testing input size: 2^$n ($SIZE elements)" | tee -a "$RESULTS_FILE"

    for TYPE in "int" "float"; do
        echo "Data type: $TYPE" | tee -a "$RESULTS_FILE"

        # Only generate once per size/type
        INPUT_FILE="input_${TYPE}_${SIZE}.npy"
        if [ ! -f "$INPUT_FILE" ]; then
            echo "Generating input data: $INPUT_FILE"
            python3 -c "import numpy as np; np.save('$INPUT_FILE', np.random.randint(0, 100, $SIZE) if '$TYPE'=='int' else np.random.rand($SIZE).astype('float64'))"
        fi

        # Run each algorithm and time it
        for ALG in "$ALG1" "$ALG2" "$ALG3" "$ALG4"; do
            echo -n "$ALG - " | tee -a "$RESULTS_FILE"
            /usr/bin/time -f "%.3f seconds" -o temp_time.txt python3 "$ALG" "$INPUT_FILE"
            cat temp_time.txt | tee -a "$RESULTS_FILE"
        done
    done

    echo "------------------------------------------" | tee -a "$RESULTS_FILE"
done

rm -f temp_time.txt