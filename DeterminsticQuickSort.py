def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Select the pivot (last element in this case)
    pivot = arr[high]
    i = low - 1  # Index of the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
