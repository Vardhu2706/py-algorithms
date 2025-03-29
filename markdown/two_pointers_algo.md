# Two Pointers Algorithm

```python
```python
# Two Pointers Algorithm

## 1. Category / Type
"""
The Two Pointers algorithm is a technique often used for solving problems related to arrays or linked lists, where two pointers are used to iterate through the data structure, usually from different ends or at different speeds.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Two Pointers algorithm is to use two separate pointers to traverse a data structure simultaneously. By moving these pointers under certain conditions, we can efficiently solve problems that involve finding pairs that satisfy a given condition, merging sorted lists, or reversing data structures in place. This method often reduces the need for nested iterations, thus optimizing time complexity.
"""

## 3. Steps / Flow
"""
1. Initialize two pointers, often `left` and `right`, at the beginning and end of the data structure, or at different positions as required by the problem.
2. Iterate through the data structure based on a condition:
   - Move one or both pointers towards each other or in a specific manner, depending on the conditions being checked.
   - Perform operations or checks, such as summing values, comparing elements, or swapping values.
3. Continue the iteration until the pointers meet or cross each other, or until a solution is found.
4. Return the required result, which could be a boolean, a pair of indices, or a modified data structure.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space |
|-----------|-----------|-----------|-------|
| O(n)      | O(n)      | O(n)      | O(1)  |
- Time complexity is generally linear, O(n), because each element is visited at most once by each pointer.
- Space complexity is O(1) when no additional data structures are used.
"""

## 5. Use Cases
"""
- Finding pairs in an array that sum up to a specific target.
- Partitioning an array around a pivot.
- Merging two sorted lists or arrays.
- Detecting a cycle in a linked list (Floyd’s Tortoise and Hare algorithm).
- Reversing a sequence in place.
"""

## 6. Common Variants
"""
- Slow and Fast Pointers: One pointer moves at a double speed compared to the other, useful in cycle detection.
- Same Direction Pointers: Both pointers start from the same end and move in the same direction, used in sliding window problems.
"""

## 7. Trade-offs
"""
- While the two pointers technique can be space-efficient (O(1) space), it might not always be suitable for data structures where random access is not feasible, such as linked lists.
- The technique relies on the ability to iterate over the data structure in a linear manner, which may not be possible in all problem scenarios.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that the pointers are initialized correctly and that boundary conditions are handled to avoid out-of-bounds errors.
- Be cautious of infinite loops by ensuring that pointers are moved correctly in each iteration.
- Special care is needed when dealing with data structures that contain duplicates or require specific order maintenance.
"""

## 9. Classic Problems
"""
- Two Sum: Find two numbers in an array that add up to a specific target.
- Container With Most Water: Find two lines that together with the x-axis form a container that holds the most water.
- Palindrome Check: Use two pointers to compare characters from the beginning and end of a string.
"""

## 10. Code Implementation (Demo)
def two_sum(nums, target):
    nums.sort()  # Sort the array first
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []  # Return an empty list if no pair is found
```
```