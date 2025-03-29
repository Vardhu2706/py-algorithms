# Heap Sort Algorithm

## 1. Category / Type
"""
Heap Sort is a comparison-based sorting algorithm that falls under the category of 'Divide and Conquer' algorithms.
It utilizes a binary heap data structure to organize and sort data efficiently.
"""

## 2. Core Idea / Intuition
"""
The core idea of Heap Sort is to leverage the properties of a binary heap to sort an array. A binary heap is a complete binary tree where each node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap). Heap Sort typically uses a max-heap to sort an array in ascending order.

The algorithm consists of two main phases:
1. **Build a max heap** from the input data.
2. **Extract elements** one by one from the heap to get them in sorted order.
"""

## 3. Steps / Flow
"""
1. **Build Max Heap**: 
   - Convert the input array into a max heap. This can be done in O(n) time using the bottom-up heap construction method.
   
2. **Heap Sort**:
   - Repeat the following until the heap is empty:
     - Swap the root of the heap (maximum value) with the last element of the heap.
     - Reduce the size of the heap by one, effectively removing the last element from the heap.
     - Call heapify on the root to maintain the max heap property.

The array is now sorted in ascending order.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space  |
|---------|---------|---------|--------|
| O(n log n) | O(n log n) | O(n log n) | O(1)  |
"""

## 5. Use Cases
"""
- Suitable for large datasets where O(n log n) time complexity is acceptable.
- Useful in systems where O(1) space complexity is a priority.
- Often employed in real-time systems due to its predictable performance.
"""

## 6. Common Variants
"""
- **Min-Heap Sort**: Uses a min-heap to sort data in descending order.
- **External Heap Sort**: Used for sorting data that does not fit into memory.
"""

## 7. Trade-offs
"""
- **Pros**: 
  - In-place sorting algorithm with O(1) auxiliary space.
  - Consistent O(n log n) time complexity in all cases.

- **Cons**:
  - Not a stable sort, meaning the relative order of equal elements may not be preserved.
  - Generally slower in practice compared to other O(n log n) algorithms like Quick Sort and Merge Sort due to poor cache performance.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that heapify is implemented correctly to maintain the heap property throughout the sorting process.
- Be cautious of off-by-one errors when dealing with array indices during heap operations.
"""

## 9. Classic Problems
"""
- **Priority Queue**: Heap Sort is closely related to the implementation of priority queues.
- **Kth Largest Element**: Can be efficiently solved using a heap-based approach.
"""

## 10. Code Implementation (Demo)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example usage
data = [12, 11, 13, 5, 6, 7]
heap_sort(data)
print("Sorted array is", data)
