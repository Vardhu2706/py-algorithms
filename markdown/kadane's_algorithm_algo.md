# Kadane's Algorithm Algorithm

```python
```python
# Kadane's Algorithm

## 1. Category / Type
"""
Kadane's Algorithm is a Dynamic Programming algorithm that solves the Maximum Subarray Problem.
"""

## 2. Core Idea / Intuition
"""
The core idea of Kadane's Algorithm is to find the maximum sum of a contiguous subarray in a given one-dimensional numeric array. 
It does this by iterating through the array while maintaining the maximum sum found so far and the current subarray sum. 
The algorithm exploits the fact that a positive sum can contribute positively to the total sum, while a negative sum should be discarded.
"""

## 3. Steps / Flow
"""
1. Initialize two variables: max_so_far and max_ending_here. Set both to the first element of the array.
2. Iterate through the array starting from the second element:
   - For each element, update max_ending_here with the maximum of the current element itself or the sum of max_ending_here and the current element.
   - Update max_so_far to be the maximum value between max_so_far and max_ending_here.
3. Continue this process until the end of the array.
4. At the end of the iteration, max_so_far will hold the maximum sum of the contiguous subarray.
"""

## 4. Time & Space Complexity
"""
| Best   | Average | Worst  | Space |
|--------|---------|--------|-------|
| O(n)   | O(n)    | O(n)   | O(1)  |
- Time complexity is linear because the array is traversed once.
- Space complexity is constant as only a fixed number of variables are used.
"""

## 5. Use Cases
"""
- Finding the maximum profit from stock price changes within a single day.
- Detecting the subarray with the highest cumulative temperature change.
- Analyzing signal strength over time to find optimal periods.
"""

## 6. Common Variants
"""
- 2D Maximum Subarray Problem: Extends Kadane's Algorithm to two dimensions to find the maximum sum rectangle in a 2D array.
- Circular Maximum Subarray: Finds the maximum sum of a subarray in a circular array.
"""

## 7. Trade-offs
"""
- Kadane's Algorithm assumes the array has at least one non-negative number. If all numbers are negative, it will return the least negative number.
- It only works for numeric arrays and does not provide subarray indices without modification.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure the array is not empty before applying the algorithm, as accessing the first element directly can lead to errors.
- If all numbers in the array are negative, the algorithm will still return the largest (least negative) number, which may not be intuitive.
"""

## 9. Classic Problems
"""
- The Maximum Subarray Problem is a classic problem in computer science that can be solved efficiently using Kadane's Algorithm.
- Variations of this problem can be found in competitive programming and technical interviews.
"""

## 10. Code Implementation (Demo)
def kadane_algorithm(arr):
    if not arr:
        return 0  # Return 0 if the array is empty

    max_so_far = arr[0]
    max_ending_here = arr[0]

    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```
```