from DeterminsticQuickSort import quicksort

import time
import random
import sys

# Increase recursion limit
sys.setrecursionlimit(20000)  # Adjust this value as needed based on array size

# Define a function to measure execution time of deterministic quicksort
def measure_sort_time(arr):
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Deterministic Quicksort functions (same as before)
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test arrays with different cases
array_sizes = [1000, 5000, 10000]  # Testing with different input sizes

# 1. Empty array test
empty_array = []
time_empty = measure_sort_time(empty_array)
print(f"Empty array sorted in: {time_empty:.6f} seconds")

# Loop through other test arrays with increasing sizes
for size in array_sizes:
    # 2. Randomly generated array
    random_array = [random.randint(1, 10000) for _ in range(size)]
    time_random = measure_sort_time(random_array)
    print(f"Random array of size {size} sorted in: {time_random:.6f} seconds")

    # 3. Already sorted array
    sorted_array = list(range(1, size + 1))
    time_sorted = measure_sort_time(sorted_array)
    print(f"Sorted array of size {size} sorted in: {time_sorted:.6f} seconds")

    # 4. Reverse-sorted array
    reverse_sorted_array = list(range(size, 0, -1))
    time_reverse_sorted = measure_sort_time(reverse_sorted_array)
    print(f"Reverse sorted array of size {size} sorted in: {time_reverse_sorted:.6f} seconds")

    # 5. Array with repeated elements
    repeated_elements_array = [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
    time_repeated = measure_sort_time(repeated_elements_array)
    print(f"Array with repeated elements of size {size} sorted in: {time_repeated:.6f} seconds")

    print("-" * 40)
