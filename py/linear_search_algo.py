# Linear Search Algorithm

## 1. Category / Type
"""
Linear Search is a type of Search algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea behind Linear Search is to traverse the list sequentially and check each element until the target value is found or the end of the list is reached. It is straightforward and does not require the list to be sorted.
"""

## 3. Steps / Flow
"""
1. Start from the first element of the list.
2. Compare the current element with the target value:
   - If they are equal, return the current index.
   - If they are not equal, move to the next element.
3. Repeat step 2 until the end of the list is reached.
4. If the target value is not found in the list, return -1 to indicate that the target does not exist in the list.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space |
|---------|---------|---------|-------|
| O(1)    | O(n)    | O(n)    | O(1)  |

- Best case occurs when the target element is at the first position of the list.
- Average and worst cases occur when the target is located towards the end of the list or is not present.
- Space complexity is O(1) because no additional storage is needed beyond the input list.
"""

## 5. Use Cases
"""
- Suitable for small to medium-sized lists where simplicity is more important than performance.
- Useful when dealing with unsorted lists where sorting is not feasible or necessary.
- Applied when the list size is manageable and the overhead of more complex search algorithms is not warranted.
"""

## 6. Common Variants
"""
- Sentinel Linear Search: A variant where a sentinel (extra element) is added to the end of the list to eliminate the boundary checking during the search.
- Bidirectional Linear Search: Two pointers are used, one starting from the beginning and the other from the end, reducing the search space more quickly.
"""

## 7. Trade-offs
"""
- Pros:
  - Simple to implement and understand.
  - Does not require sorted data.
  - Performs well with small datasets.

- Cons:
  - Inefficient for large datasets due to O(n) time complexity in the average and worst cases.
  - Other search algorithms like Binary Search are more efficient for large, sorted datasets.
"""

## 8. Pitfalls / Gotchas
"""
- Inefficiency with large datasets: Linear search can be slow with large lists because it potentially examines every element.
- Assumes access to data: The algorithm assumes that accessing each element of the list is equally costly, which might not hold true in some data structures.
"""

## 9. Classic Problems
"""
- Finding a specific element in an unsorted list.
- Checking if a list contains a duplicate element.
- Verifying the existence of a particular value in a dataset.
"""

## 10. Code Implementation (Demo)
def linear_search(arr, target):
    """
    Performs a linear search for a target value in a list.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
