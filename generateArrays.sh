#!/bin/bash


OUTPUT_DIR="intarrays"
OUTPUT_DIR2="floatarrays"
mkdir -p "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR2"

START=29
END=30

# generate arrays from 2^start to 2^end (IF YOU JUST WANT TO GENERATE ALL, CHANGE START TO 20 AND END TO 30. I RECCOMEND YOU USE MINE FROM DRIVE AND ONLY RUN THIS FOR 29,30)
for ((i=START; i<=END; i++)); do
    SIZE=$((2 ** i))
    FILENAME="$OUTPUT_DIR/array_2^$i.npy"
    FILENAME2="$OUTPUT_DIR2/array_2^$i.npy"

    echo "Generating array of size 2^$i ($SIZE)..."

# THESE SIMPLY RUN THE QUOTED CODE. FILES ARE SAVED TO THEIR RESPECTIVE DIRECTORIES IMPLICITLY BY ASSIGNATION OF FILENAME

    python3 -c "
import numpy as np
a = np.random.rand($SIZE).astype(np.int64)
np.save('$FILENAME', a)
"
    python3 -c "
import numpy as np
a = np.random.rand($SIZE).astype(np.float64)
np.save('$FILENAME2', a)
"

    echo "Saved to $FILENAME"
    echo "Saved to $FILENAME2"
done

echo "arrays generated in the '$OUTPUT_DIR' and '$OUTPUT_DIR2' directory."