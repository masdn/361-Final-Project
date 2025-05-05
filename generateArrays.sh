#!/bin/bash


OUTPUT_DIR="arrays"
mkdir -p "$OUTPUT_DIR"

START=20
END=30

# generate arrays from 2^20 to 2^30
for ((i=START; i<=END; i++)); do
    SIZE=$((2 ** i))
    FILENAME="$OUTPUT_DIR/array_2^$i.npy"

    echo "Generating array of size 2^$i ($SIZE)..."

    python3 -c "
import numpy as np
a = np.random.rand($SIZE).astype(np.float64)
np.save('$FILENAME', a)
"

    echo "Saved to $FILENAME"
done

echo "arrays generated in the '$OUTPUT_DIR' directory."