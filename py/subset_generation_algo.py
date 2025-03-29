# Subset Generation Algorithm

## 1. Category / Type
"""
- Combinatorial Algorithms
- Backtracking
- Recursive Algorithms
"""

## 2. Core Idea / Intuition
"""
The main idea behind subset generation is to explore all possible subsets of a given set. This is a classical combinatorial problem where the goal is to generate all combinations of a set's elements. For a set with `n` elements, there are `2^n` possible subsets, including the empty set and the set itself.

The algorithm leverages the concept of recursion and backtracking to systematically explore each subset possibility. At each step, the algorithm decides whether to include a particular element in the current subset or not, proceeding recursively to explore further possibilities.
"""

## 3. Steps / Flow
"""
1. **Initialize**:
   - Begin with an empty list to store all subsets.
   - Define a recursive function that explores each subset possibility.

2. **Recursive Function**:
   - Base Case: If the end of the set is reached, add the current subset to the list of all subsets.
   - Recursive Case: 
     - Exclude the current element and recursively process the remaining elements.
     - Include the current element in the current subset and recursively process the remaining elements.

3. **Backtrack**:
   - Once a subset is fully explored, backtrack by removing the last added element and explore other possibilities.

4. **Output**:
   - After all recursive calls complete, the list of all subsets contains all possible subsets of the original set.
"""

## 4. Time & Space Complexity
"""
| Best   | Average | Worst  | Space   |
|--------|---------|--------|---------|
| O(2^n) | O(2^n)  | O(2^n) | O(n*2^n) |

- Time Complexity: The algorithm generates all `2^n` subsets.
- Space Complexity: Each subset can take up to `n` space, leading to an overall space complexity of `O(n*2^n)`.
"""

## 5. Use Cases
"""
- Power set generation for mathematical analysis.
- Feature selection in machine learning where all combinations of features are explored.
- Solving problems in decision-making and optimization where all possible states need to be considered.
"""

## 6. Common Variants
"""
- Subset generation with specific constraints (e.g., subsets of a given size).
- Subset generation for multi-set (sets with duplicate elements).
- Permutation generation, which is related but focuses on ordered arrangements.
"""

## 7. Trade-offs
"""
- The power of subset generation lies in its exhaustive exploration, but this can be computationally expensive for large sets due to exponential growth in the number of subsets.
- The algorithm is simple and elegant but may not be suitable for very large datasets due to memory and time constraints.
"""

## 8. Pitfalls / Gotchas
"""
- The exponential growth in the number of subsets can lead to high memory usage and execution time.
- Ensuring subsets are unique when dealing with multi-sets requires additional handling.
- Recursive implementations may hit recursion depth limits in Python for very large sets.
"""

## 9. Classic Problems
"""
- Generating power sets, a fundamental problem in combinatorics.
- Solving the subset sum problem by exploring all possible subsets.
- Finding all possible combinations of items for knapsack-type problems.
"""

## 10. Code Implementation (Demo)

def generate_subsets(nums):
    def backtrack(index, current_subset):
        # If we have considered all elements
        if index == len(nums):
            # Add a copy of the current subset to the list of all subsets
            all_subsets.append(current_subset[:])
            return
        
        # Decision not to include nums[index]
        backtrack(index + 1, current_subset)
        
        # Decision to include nums[index]
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()  # Backtrack

    all_subsets = []
    backtrack(0, [])
    return all_subsets

# Example usage
nums = [1, 2, 3]
print(generate_subsets(nums))
