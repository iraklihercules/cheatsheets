# bubble_sort function: Implements the bubble sort algorithm.
# arr: The list to be sorted.
# n: Length of the array.
# The outer loop iterates through each element of the array.
# The inner loop iterates through the unsorted part of the array and compares adjacent elements.
# If the current element is greater than the next element, they are swapped.

# Bubble sort is not the most efficient sorting algorithm, as it has a time complexity of O(n^2)
# in the worst case. However, it is relatively simple to implement and understand, making it a
# good choice for educational purposes or small datasets.


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)

    print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
