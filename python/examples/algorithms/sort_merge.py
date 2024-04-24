# merge_sort function: Implements the merge sort algorithm.
# arr: The list to be sorted.
# The function recursively divides the array into two halves until each half contains only one element.
# Then, it merges the sorted halves back together by comparing elements and placing them in the correct order.

# Merge sort is a divide-and-conquer algorithm that has a time complexity of O(n log n) in all cases.
# It is efficient for sorting large datasets and is stable, meaning it preserves the relative order of equal
# elements in the sorted output.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call to sort the left half
        merge_sort(right_half)  # Recursive call to sort the right half

        # Merge the sorted halves
        i = j = k = 0  # Initialize indices for left_half, right_half, and arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are remaining in the left_half or right_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)

    print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

