# selection_sort function: Implements the selection sort algorithm.
# arr: The list to be sorted.
# n: Length of the array.
# The outer loop iterates through each element of the array.
# In each iteration, the inner loop finds the minimum element in the unsorted part of the array.
# The minimum element is then swapped with the first element of the unsorted part.

# Selection sort is also not the most efficient sorting algorithm, as it has a time complexity of O(n^2)
# in the worst case. However, it performs fewer swaps compared to bubble sort, making it more efficient
# for arrays with large data but a small number of swaps.

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)

    print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
