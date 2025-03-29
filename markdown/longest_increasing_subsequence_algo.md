# Longest Increasing Subsequence Algorithm

```python
# Longest Increasing Subsequence Algorithm

## 1. Category / Type
"""
The Longest Increasing Subsequence (LIS) algorithm falls under the category of Dynamic Programming and Combinatorial Optimization.
"""

## 2. Core Idea / Intuition
"""
The core idea behind the Longest Increasing Subsequence algorithm is to identify a subsequence within a sequence of numbers where the elements are in increasing order and the subsequence has the maximum possible length. The algorithm achieves this by exploring all possible subsequences and efficiently determining the longest one using dynamic programming techniques.

Intuitively, for each element in the sequence, the algorithm determines the longest increasing subsequence that ends with that element. By leveraging previously computed results, it avoids recomputing solutions for overlapping subproblems.
"""

## 3. Steps / Flow
"""
1. Initialize a list, `dp`, where `dp[i]` represents the length of the longest increasing subsequence that ends at index `i`.
2. Set each element of `dp` to 1, as each element is a subsequence of length 1 by itself.
3. Iterate over each element in the sequence from left to right:
   - For each element at index `i`, iterate over all elements before it (index `j` where `0 <= j < i`):
     - If the element at `i` is greater than the element at `j`, update `dp[i]` as:
       `dp[i] = max(dp[i], dp[j] + 1)`
4. The length of the longest increasing subsequence is the maximum value in the `dp` array.
"""

## 4. Time & Space Complexity
"""
| Best   | Average  | Worst   | Space  |
|--------|----------|---------|--------|
| O(n^2) | O(n^2)   | O(n^2)  | O(n)   |
"""

## 5. Use Cases
"""
- Determining the longest trend of increasing stock prices.
- Analyzing sequences in bioinformatics, such as DNA or protein sequences.
- Evaluating performance trends in sports or academics over time.
"""

## 6. Common Variants
"""
- Longest Decreasing Subsequence: Find the longest subsequence where elements are in decreasing order.
- Finding the actual subsequence: Not just the length, but also the sequence of elements.
- Patience Sorting Algorithm: An advanced method using binary search with a time complexity of O(n log n).
"""

## 7. Trade-offs
"""
- The O(n^2) dynamic programming approach is straightforward and easier to implement but can be slow for large datasets.
- The O(n log n) patience sorting method is faster but more complex and harder to understand and implement correctly.
"""

## 8. Pitfalls / Gotchas
"""
- Handling edge cases where the sequence is empty or has only one element.
- Ensuring that the subsequences are strictly increasing, not just non-decreasing.
- Avoiding off-by-one errors when iterating through the sequence.
"""

## 9. Classic Problems
"""
- The "Russian Doll Envelopes" problem, which involves nesting envelopes inside each other based on size.
- The "Maximum Sum Increasing Subsequence" problem, where the objective is to find the subsequence with the maximum sum rather than length.
"""

## 10. Code Implementation (Demo)
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
sequence = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of Longest Increasing Subsequence is:", longest_increasing_subsequence(sequence))
```