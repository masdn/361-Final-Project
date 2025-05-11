if __name__ == "__main__":
    file = sys.argv[1]
    arr = np.load(file)
    times = []

    start = time.time() 
    sortedArr = threeWay(arr.tolist())
    end = time.time()
    timeF = end - start
    times[0] = timeF

    start = time.time()
    # your function
    end = time.time()
    timeF = end - start
    times[1] = timeF

    #repeat for other functions. this file is to satisfy the requirement that we have 
    #a "function" that runs all of the programs and benchmarks them and provides output, 
    #whatever that fuckin means. lets not ever actually use this because our computers would melt.


    print("Three way sorted {file} in {timeF} seconds.\n", file, times[0])