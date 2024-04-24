# insert(data): Inserts a new element into the max-heap while maintaining the max-heap property.
# _heapify_up(index): Restores the max-heap property by moving the inserted element up the heap if necessary.
# extract_max(): Removes and returns the maximum value from the max-heap while maintaining the max-heap property.
# _heapify_down(index): Restores the max-heap property by moving the element at the given index down the heap if necessary.
# get_max(): Returns the maximum value in the max-heap without removing it.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def get_max(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None


# Example usage:
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(7)
    max_heap.insert(2)
    max_heap.insert(4)

    print("Max heap:")
    print("Extracted max:", max_heap.extract_max())  # Output: 7
    print("Max heap after extracting max:", max_heap.heap)  # Output: [5, 4, 3, 2]
    print("Max value:", max_heap.get_max())  # Output: 5
