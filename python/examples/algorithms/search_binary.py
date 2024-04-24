# binary_search function: Implements the binary search algorithm.
# arr: The list to be searched (must be sorted in ascending order).
# target: The element to search for.
# The function maintains two pointers, left and right, representing the boundaries of the search range.
# It repeatedly divides the search range in half by calculating the middle index (mid).
# If the middle element is equal to the target, it returns the index of the target element.
# If the target is smaller than the middle element, it updates the right pointer to search in the left half.
# If the target is greater than the middle element, it updates the left pointer to search in the right half.
# The process continues until the target element is found or the search range is empty.

# Binary search is an efficient searching algorithm with a time complexity of O(log n),
# where n is the number of elements in the array. It repeatedly divides the search range in half,
# effectively reducing the search space with each iteration. However, it requires the array to be sorted
# beforehand.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Return the index of the target element if found
        elif arr[mid] < target:
            left = mid + 1  # Update the left boundary if the target is greater than the middle element
        else:
            right = mid - 1  # Update the right boundary if the target is smaller than the middle element

    return -1  # Return -1 if the target element is not found


# Example usage:
if __name__ == "__main__":
    arr = [11, 12, 22, 25, 34, 64, 90]
    target = 22
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
