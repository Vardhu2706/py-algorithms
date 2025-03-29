# Insertion Sort Algorithm

## 1. Category / Type
"""
Sorting Algorithm, Comparison Sort, In-place Algorithm
"""

## 2. Core Idea / Intuition
"""
Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it has the advantage of being simple, easy to implement, and efficient for small data sets or partially sorted data.

The core idea is to iterate through the array and at each position, assume that all elements before it are sorted. Then, take the element at the current position and insert it into the correct position within the sorted portion of the array.
"""

## 3. Steps / Flow
"""
1. Start with the first element in the array as a sorted portion.
2. Take the next element and store it in a temporary variable (key).
3. Compare the key with each element in the sorted portion (to its left) from right to left.
4. Shift elements that are greater than the key to the right.
5. Insert the key into its correct position.
6. Repeat steps 2-5 for all elements in the array.

Example:
Given array: [5, 2, 4, 6, 1, 3]
- Start with first element [5] as sorted.
- Next element 2 is compared with 5. Insert 2 before 5: [2, 5]
- Next element 4 is compared with 5. Insert 4 before 5: [2, 4, 5]
- Continue this process until the array is fully sorted: [1, 2, 3, 4, 5, 6]
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space |
|---------|---------|---------|-------|
| O(n)    | O(n^2)  | O(n^2)  | O(1)  |
"""

## 5. Use Cases
"""
- Suitable for small datasets due to simplicity.
- Efficient for datasets that are already substantially sorted (nearly sorted).
- Used in hybrid sorting algorithms like Timsort, which is implemented in Python's built-in sort.
"""

## 6. Common Variants
"""
- Binary Insertion Sort: Uses binary search to find the correct location to insert the current element, reducing the number of comparisons in some cases.
- Shell Sort: Generalization of insertion sort that allows the exchange of items that are far apart.
"""

## 7. Trade-offs
"""
- Simple to implement and understand.
- Not suitable for large datasets due to quadratic time complexity.
- Performs efficiently on small or nearly sorted datasets.
- In-place and stable sort: does not require additional memory and maintains the relative order of equal elements.
"""

## 8. Pitfalls / Gotchas
"""
- Poor performance on large, randomly ordered datasets.
- May be outperformed by more complex algorithms like quicksort or mergesort on larger datasets.
- While insertion sort is stable, modifications or variants of the algorithm might not preserve stability.
"""

## 9. Classic Problems
"""
- Used as a teaching tool to explain the fundamentals of sorting algorithms.
- Often used in scenarios where the cost of writing complex algorithms is not justified by the small size of the input data.
"""

## 10. Code Implementation (Demo)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
