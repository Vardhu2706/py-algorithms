# Selection Sort Algorithm

```python
```python
# Selection Sort Algorithm

## 1. Category / Type
"""
Selection Sort is a comparison-based sorting algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of Selection Sort is to divide the array into two parts: a sorted and an unsorted subarray. The algorithm repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted subarray and swaps it with the leftmost unsorted element, effectively growing the sorted subarray from left to right.
"""

## 3. Steps / Flow
"""
1. Start with the first element as the initial sorted portion of the array.
2. Iterate over the unsorted portion of the array to find the minimum element.
3. Swap the found minimum element with the first element of the unsorted portion.
4. Move the boundary of the sorted portion one element to the right.
5. Repeat until the entire array is sorted.

For an array of length `n`:
- For `i` from `0` to `n-1`:
  - Assume the minimum element is at index `i`.
  - For each `j` from `i+1` to `n-1`, if `array[j]` is less than `array[min_index]`, update `min_index`.
  - Swap `array[i]` and `array[min_index]`.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space |
|---------|---------|---------|-------|
| O(n^2)  | O(n^2)  | O(n^2)  | O(1)  |
"""

## 5. Use Cases
"""
- Suitable for small datasets where the simplicity of implementation is more critical than performance.
- When memory space is limited, as it is an in-place sorting algorithm.
- Educational purposes to understand the fundamentals of sorting algorithms.
"""

## 6. Common Variants
"""
- Bidirectional Selection Sort: Finds both the minimum and maximum elements in the unsorted part and places them at their correct positions in each iteration.
- Recursive Selection Sort: Implements the selection sort algorithm using recursion instead of loops.
"""

## 7. Trade-offs
"""
- Selection Sort has a fixed time complexity of O(n^2), making it inefficient for large datasets compared to more advanced algorithms like QuickSort or MergeSort.
- It performs well on small lists and is easy to implement and understand.
- It does not require additional memory space for sorting, as it is an in-place algorithm. However, it is not stable, meaning that the relative order of equal elements may not be preserved.
"""

## 8. Pitfalls / Gotchas
"""
- The algorithm always runs in O(n^2) time, regardless of the input array's initial order.
- It is not a stable sort, which means it does not maintain the relative order of records with equal keys.
- Not suitable for large datasets due to its quadratic time complexity.
"""

## 9. Classic Problems
"""
- Sorting small arrays or lists where the overhead of more complex algorithms is not justified.
- Teaching fundamental sorting algorithm concepts and in-place sorting techniques.
"""

## 10. Code Implementation (Demo)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```
```