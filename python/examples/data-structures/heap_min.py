# insert(data): Inserts a new element into the min-heap while maintaining the min-heap property.
# _heapify_up(index): Restores the min-heap property by moving the inserted element up the heap if necessary.
# extract_min(): Removes and returns the minimum value from the min-heap while maintaining the min-heap property.
# _heapify_down(index): Restores the min-heap property by moving the element at the given index down the heap if necessary.
# get_min(): Returns the minimum value in the min-heap without removing it.

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None


# Example usage:
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.insert(2)
    min_heap.insert(4)

    print("Min heap:")
    print("Extracted min:", min_heap.extract_min())  # Output: 2
    print("Min heap after extracting min:", min_heap.heap)  # Output: [3, 4, 7, 5]
    print("Min value:", min_heap.get_min())  # Output: 3
