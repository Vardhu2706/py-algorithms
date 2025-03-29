# Merge Sort Algorithm

```python
```python
# Merge Sort Algorithm

## 1. Category / Type
"""
Merge Sort is a Divide and Conquer algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of Merge Sort is to divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted), repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

Key Intuition:
- Divide: Split the array into two halves.
- Conquer: Recursively sort both halves.
- Combine: Merge the two sorted halves to produce a sorted array.
"""

## 3. Steps / Flow
"""
1. If the list is of length 0 or 1, it is already sorted. Return it.
2. Divide the unsorted list into two approximately equal halves.
3. Recursively sort the two halves.
4. Merge the two sorted halves to produce a single sorted list.
5. During the merge process, repeatedly compare the smallest elements of each half and append the smaller element to the result list.
6. If one of the halves is exhausted before the other, append the remaining elements of the non-exhausted half to the result list.
"""

## 4. Time & Space Complexity
"""
| Best       | Average   | Worst     | Space    |
|------------|-----------|-----------|----------|
| O(n log n) | O(n log n)| O(n log n)| O(n)     |
"""

## 5. Use Cases
"""
- Sorting large datasets where the additional space complexity of O(n) is not a constraint.
- When stable sorting is required (i.e., equal elements retain their relative order post-sort).
- Useful in scenarios where data is accessed sequentially rather than randomly.
"""

## 6. Common Variants
"""
- Bottom-Up Merge Sort: An iterative version that avoids the recursive overhead by using a loop to iteratively merge sublists.
"""

## 7. Trade-offs
"""
- Advantages: Consistent O(n log n) performance, stable sort, and good performance on large datasets.
- Disadvantages: Requires extra space proportional to the size of the input, which can be a drawback for large datasets on memory-constrained systems.
"""

## 8. Pitfalls / Gotchas
"""
- The extra space requirement can be significant for large datasets.
- Recursive depth can lead to stack overflow in languages with limited stack sizes if not implemented carefully.
- Care must be taken to merge the halves correctly to avoid overwriting data.
"""

## 9. Classic Problems
"""
- Sorting linked lists, where Merge Sort's non-constant extra space requirement can be mitigated.
- External sorting algorithms, where data is too large to fit into memory, and data is sorted using disk storage.
"""

## 10. Code Implementation (Demo)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
```
```