# linear_search function: Implements the linear search algorithm.
# arr: The list to be searched.
# target: The element to search for.
# The function iterates through each element of the array.
# If the current element matches the target element, it returns the index of the target element.
# If the target element is not found after traversing the entire array, it returns -1.

# Linear search is a simple and straightforward searching algorithm with a time complexity of O(n),
# where n is the number of elements in the array. It sequentially checks each element of the array
# until it finds the target element or reaches the end of the array.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not found


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    result = linear_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
