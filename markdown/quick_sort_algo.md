# Quick Sort Algorithm

```python
```python
# Quick Sort Algorithm

## 1. Category / Type
"""
Quick Sort is a comparison-based, divide-and-conquer sorting algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of Quick Sort is to select a 'pivot' element from the array and partition the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
"""

## 3. Steps / Flow
"""
1. Choose a pivot element from the array. This can be done using various strategies such as picking the first element, the last element, the middle element, or a random element.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Recursively apply the above steps to the sub-arrays.
4. Combine the sub-arrays and the pivot to form the sorted array.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space    |
|-----------|-----------|-----------|----------|
| O(n log n) | O(n log n) | O(n^2)   | O(log n) |

- Best and Average case complexities are O(n log n) because the array is divided into two nearly equal halves at each step.
- The worst-case complexity is O(n^2), which occurs when the smallest or largest element is always selected as the pivot, resulting in unbalanced partitions.
- Space complexity is O(log n) due to the recursive stack space used.
"""

## 5. Use Cases
"""
- Quick Sort is widely used in practice due to its average-case efficiency and in-place sorting capabilities.
- Suitable for arrays with large sizes and uniformly distributed elements.
- Used in systems where space optimization is crucial as it requires minimal additional space.
"""

## 6. Common Variants
"""
- Three-Way Quick Sort: Handles duplicates efficiently by partitioning the array into three parts: less than, equal to, and greater than the pivot.
- Randomized Quick Sort: Randomly selects the pivot to minimize the chances of encountering the worst-case scenario.
"""

## 7. Trade-offs
"""
- Quick Sort is faster than other O(n log n) algorithms like Merge Sort in practice due to its in-place operations, but its performance can degrade to O(n^2) in the worst-case.
- Unlike Merge Sort, Quick Sort is not stable (i.e., it does not preserve the relative order of equal elements).
"""

## 8. Pitfalls / Gotchas
"""
- Choosing a poor pivot can lead to unbalanced partitions and degrade performance to O(n^2).
- Quick Sort is not stable; if stability is required, additional steps need to be taken or a different algorithm should be used.
"""

## 9. Classic Problems
"""
- Sorting large datasets with limited memory.
- Part of the standard libraries in many programming languages due to its efficiency.
"""

## 10. Code Implementation (Demo)
def quick_sort(arr):
    """Sorts an array using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
```
```