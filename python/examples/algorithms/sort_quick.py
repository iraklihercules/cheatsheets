# quick_sort function: Implements the quick sort algorithm.
# arr: The list to be sorted.
# If the length of the array is 1 or less, it is already sorted, so the function returns the array.
# Otherwise, it chooses a pivot element (in this implementation, the middle element).
# It then partitions the array into three subarrays: elements smaller than the pivot, elements equal to
# the pivot, and elements greater than the pivot.
# Finally, it recursively applies quick sort to the left and right subarrays and concatenates the sorted
# subarrays with the pivot in the middle.

# Quick sort is a divide-and-conquer algorithm with an average time complexity of O(n log n).
# It is efficient for sorting large datasets and has good average-case performance. However,
# its worst-case time complexity is O(n^2) when the pivot selection is poor, making it less desirable for certain datasets.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)

    print("Sorted array:", sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
