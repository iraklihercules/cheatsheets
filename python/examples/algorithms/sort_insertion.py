# Insertion_sort function: Implements the insertion sort algorithm.
# arr: The list to be sorted.
# The outer loop iterates through each element of the array starting from the second element.
# In each iteration, the current element (key) is compared with the elements before it.
# Elements greater than the key are shifted one position to the right to make space for the key.
# The key is then placed at the correct position in the sorted subarray.

# Insertion sort is also not the most efficient sorting algorithm, as it has a time complexity of O(n^2)
# in the worst case. However, it performs well for small datasets or nearly sorted arrays.
# Additionally, it has an advantage of sorting the array in-place, meaning it requires only a constant
# amount of additional memory space.

def insertion_sort(arr):
    # Traverse through all array elements starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)

    print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
