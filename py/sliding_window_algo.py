# Sliding Window Algorithm

## 1. Category / Type
"""
- Category: Data Structure & Algorithm
- Type: Optimization Technique
"""

## 2. Core Idea / Intuition
"""
The sliding window algorithm is an optimization technique used to solve problems involving arrays or lists. The core idea is to maintain a subset of elements within a window, which 'slides' over the data structure to process elements efficiently, without the need to repeatedly process the entire subset. This technique is particularly useful when trying to find a substructure (e.g., subarray, substring) with certain properties, such as the maximum sum or a specific length.
"""

## 3. Steps / Flow
"""
1. Initialize two pointers representing the start and end of the window.
2. Traverse the array with the end pointer to expand the window.
3. Check if the current window satisfies the desired condition (e.g., sum, length).
4. If the condition is satisfied, update the result if necessary, and then move the start pointer to shrink the window.
5. Continue adjusting the start and end pointers until you have traversed the entire array.
6. Return the result obtained during the traversal.

The algorithm dynamically adjusts the window size by expanding and contracting the window to optimize the solving of the problem.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst    | Space  |
|---------|---------|----------|--------|
| O(n)    | O(n)    | O(n)     | O(1)   |

- Here, 'n' is the number of elements in the array.
- The sliding window technique typically processes each element a constant number of times, resulting in linear time complexity.
"""

## 5. Use Cases
"""
- Finding the maximum or minimum sum of any subarray of size `k`.
- Detecting a substring with all unique characters.
- Solving problems involving subarrays or substrings with specific properties, such as longest or shortest lengths.
"""

## 6. Common Variants
"""
- Fixed-size Sliding Window: Where the window size is constant, often used for problems like maximum sum of subarray of length `k`.
- Dynamic-size Sliding Window: Where the window size can change based on conditions, useful for problems like finding the smallest subarray with a sum greater than a given number.
"""

## 7. Trade-offs
"""
- The sliding window technique is generally very efficient for problems that can be expressed in terms of contiguous substructures, but it may not be suitable for non-contiguous problems.
- It reduces the time complexity compared to a naive approach but requires careful handling of pointers to ensure correctness.
"""

## 8. Pitfalls / Gotchas
"""
- Off-by-one errors: Properly managing the start and end pointers is crucial to avoid overlooking elements or accessing out-of-bounds indices.
- Ensuring the window is adjusted correctly according to problem constraints (e.g., shrinking the window correctly when a condition is met).
"""

## 9. Classic Problems
"""
- Maximum sum of a subarray of size `k`.
- Longest substring with at most `k` distinct characters.
- Smallest subarray with a sum greater than a given value.
"""

## 10. Code Implementation (Demo)
def max_sum_subarray(arr, k):
    """
    Finds the maximum sum of a subarray with size k.
    
    Parameters:
    arr (list of int): The list of integers.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of the subarray of size k.
    """
    # Check if the length of the array is less than k
    if len(arr) < k:
        return None
    
    # Initialize the maximum sum and current sum of the window
    max_sum = float('-inf')
    window_sum = 0
    
    # Start with the first k elements
    for i in range(k):
        window_sum += arr[i]
    
    # Slide the window from start to end of the array
    for i in range(k, len(arr)):
        # Update the maximum sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)
        
        # Slide the window forward by one element
        window_sum += arr[i] - arr[i - k]
    
    # Check for the last window
    max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9
