# Binary Search Algorithm

## 1. Category / Type
"""
- Search Algorithm
- Divide and Conquer
"""

## 2. Core Idea / Intuition
"""
Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the portion of the list that could contain the item in half until you've narrowed down the possible locations to just one.

The core intuition behind Binary Search is that by leveraging the sorted order of the list, we can eliminate half of the remaining elements from consideration with each comparison.
"""

## 3. Steps / Flow
"""
1. **Initialization**: Set two pointers, `low` and `high`, to the beginning and end of the list, respectively.

2. **Iteration**:
   - While `low` is less than or equal to `high`:
     - Calculate the middle index: `mid = (low + high) // 2`.
     - Compare the middle element with the target value:
       - If the middle element is equal to the target, return the middle index.
       - If the target is less than the middle element, adjust `high` to `mid - 1`.
       - If the target is greater than the middle element, adjust `low` to `mid + 1`.

3. **Completion**: If the target is not found, return an indication of failure, typically `-1`.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space |
|---------|---------|---------|-------|
| O(1)    | O(log n)| O(log n)| O(1)  |

- **Best Case**: The target is at the middle index on the first iteration.
- **Average Case**: The search space is halved with each iteration.
- **Worst Case**: The target is not in the list, or it is at one of the ends.
- **Space Complexity**: Only a constant amount of space is used, regardless of input size.
"""

## 5. Use Cases
"""
- Searching in large datasets where the data is static and sorted.
- Real-time systems where search speed is critical.
- Applications like dictionaries, phonebooks, or databases where fast lookups are necessary.
"""

## 6. Common Variants
"""
- **Lower Bound**: Finds the first occurrence of a target value.
- **Upper Bound**: Finds the last occurrence of a target value.
- **Rotated Array Search**: Adapts binary search to find elements in a rotated sorted array.
"""

## 7. Trade-offs
"""
- **Advantages**:
  - Highly efficient for large datasets due to its logarithmic time complexity.
  - Simple to implement with a sorted array.

- **Disadvantages**:
  - Requires the list to be sorted beforehand, which may require additional preprocessing.
  - Not suitable for dynamically changing data sets, as maintaining sorted order can be costly.
"""

## 8. Pitfalls / Gotchas
"""
- Off-by-one errors: Be careful with the calculation of `mid` and the adjustment of `low` and `high`.
- Requires a sorted list: Applying binary search on an unsorted list will yield incorrect results.
- Integer overflow: In languages with fixed integer sizes, `mid = (low + high) // 2` can overflow, although Python handles this automatically.
"""

## 9. Classic Problems
"""
- **Finding an Element in a Sorted Array**: The canonical problem solved by binary search.
- **Finding Peak Element**: Using a binary search approach to find a peak element in an array.
- **Search in Rotated Sorted Array**: Finding an element in a rotated version of a sorted array, which involves a modified binary search.
"""

## 10. Code Implementation (Demo)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 4
# print(binary_search(arr, target)) # Output: 3
