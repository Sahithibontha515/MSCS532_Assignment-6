import random
import time
import tracemalloc

''' Deterministic Algorithm to find kth smallest element in an array '''
def MedianOfMedians_of_array(arr, k):
    if k < 1 or k > len(arr):
        print(f"k = {k} is out of bounds for array of length {len(arr)}")
        return None
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Step 1: Divide into groups and get medians
    medians = get_medians(arr)

    # Step 2: Find median of medians
    pivot = MedianOfMedians_of_array(medians, len(medians) // 2 + 1)

    # Step 3: Partition around pivot
    lows, pivots, highs = partition(arr, pivot)

    # Step 4: Select from appropriate partition
    if k <= len(lows):
        return MedianOfMedians_of_array(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return MedianOfMedians_of_array(highs, k - len(lows) - len(pivots))


def get_medians(arr):
    # Divide into sublists of at most 5 elements and get their medians
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    return medians


def partition(arr, pivot):
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    return lows, pivots, highs


''' Randomized Algorithm to find kth smallest element in an array '''
def randomized_quickselect(arr, k):
    if k < 1 or k > len(arr):
        print(f"k = {k} is out of bounds for array of length {len(arr)}")
        return None
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return randomized_quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_quickselect(highs, k - len(lows) - len(pivots))


def evaluate_select(arr, select_fn, k):
    tracemalloc.start()
    start_time = time.perf_counter()

    result = select_fn(arr.copy(), k)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    correct_result = sorted(arr)[k - 1]
    return {
        "is_correct": result == correct_result,
        "time_taken": end_time - start_time,
        "memory_used": peak
    }


def run_comparison(algorithm_name, select_function, datasets, k):
    print(f"\n--- {algorithm_name} ---")
    for name, data in datasets.items():
        result = evaluate_select(data.copy(), select_function, k)
        print(f"{name}")
        print(f"  Correct Result   : {result['is_correct']}")
        print(f"  Time Taken       : {result['time_taken']:.6f} seconds")
        print(f"  Memory Used      : {result['memory_used']} bytes")
        print()


if __name__ == "__main__":
    dataset_size = 1000
    k = dataset_size // 2  # 1-based index for median

    print("Data Set Size:", dataset_size)
    print("Finding", k, "th smallest element\n")

    datasets = {
        "sorted_dataset": list(range(dataset_size)),
        "reverse_dataset": list(range(dataset_size - 1, -1, -1)),
        "random_dataset": random.sample(range(1, dataset_size * 2), dataset_size),
        "repeated_dataset": [random.choice([1, 2, 3, 4, 5]) for _ in range(dataset_size)]
    }

    run_comparison("Deterministic Select (Median of Medians)", MedianOfMedians_of_array, datasets, k)
    run_comparison("Randomized Quickselect", randomized_quickselect, datasets, k)
