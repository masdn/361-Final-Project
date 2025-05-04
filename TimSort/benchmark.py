import random
import time
from typing import Callable, List
from TimSort import timsort

# === Benchmark Configuration ===
SORTING_ALGORITHMS: dict[str, Callable[[List[int]], None]] = {
    'Timsort': timsort,
    "Python built-in sort": lambda arr: arr.sort(),
    # 'MergeSort': merge_sort,
    # 'QuickSort': quick_sort,
}

INPUT_SIZES = [2 ** i for i in range(20, 31)]
SEED = 42  # for reproducibility

def benchmark_sort(
    sort_fn: Callable[[List[float]], None],
    arr: List[float],
    repeat: int = 3
) -> float:
    times = []
    for _ in range(repeat):
        data = arr.copy()
        start = time.perf_counter()
        sort_fn(data)
        end = time.perf_counter()
        times.append(end - start)
    return min(times)


def main():
    print(f"{'Size':>10} | " + " | ".join(f"{name:>18}" for name, _ in SORTING_ALGORITHMS.items()))
    print("-" * (12 + 21 * len(SORTING_ALGORITHMS.items())))
    for size in INPUT_SIZES[:5]:
        arr = [random.random() for _ in range(size)]
        results = []
        for name, fn in SORTING_ALGORITHMS.items():
            try:
                t = benchmark_sort(fn, arr)
                results.append(f"{t:>18.4f}s")
            except MemoryError:
                results.append(f"{'OOM':>18}")
            except Exception as e:
                results.append(f"{'ERR':>18}")
        print(f"{size:10} | " + " | ".join(results))


if __name__ == "__main__":
    main()
