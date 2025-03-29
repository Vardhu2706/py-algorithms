# 0/1 Knapsack Algorithm

## 1. Category / Type
"""
The 0/1 Knapsack problem falls under the category of dynamic programming. It is a combinatorial optimization problem.
"""

## 2. Core Idea / Intuition
"""
The core idea of the 0/1 Knapsack problem is to determine the maximum value that can be obtained by selecting items with given weights and values such that the total weight does not exceed a given capacity. Each item can either be included (1) or excluded (0) from the knapsack, hence the name 0/1 Knapsack. The solution uses dynamic programming to build up solutions to subproblems and reuse them to solve the larger problem efficiently.
"""

## 3. Steps / Flow
"""
- Step 1: Initialize a 2D array `dp` where `dp[i][w]` represents the maximum value that can be achieved with the first `i` items and a knapsack capacity of `w`.
- Step 2: Iterate over each item and for each weight capacity from 0 to the maximum capacity.
  - If the weight of the current item is more than the current capacity, the item cannot be included, so `dp[i][w] = dp[i-1][w]`.
  - Otherwise, calculate the maximum value by considering both including and excluding the current item: 
    `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])`.
- Step 3: The value at `dp[n][capacity]` gives the maximum value that can be obtained.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space     |
|-----------|-----------|-----------|-----------|
| O(nW)     | O(nW)     | O(nW)     | O(nW)     |

- n: Number of items
- W: Maximum capacity of the knapsack

Both time and space complexities are O(nW), as we iterate through each item and each capacity and store results in a 2D array.
"""

## 5. Use Cases
"""
- Resource allocation problems where resources have to be allocated under certain constraints.
- Financial decision-making problems where investments with certain costs and profits need to be optimized.
- In logistics, for optimizing the load in a cargo, considering weight and value.
"""

## 6. Common Variants
"""
- Fractional Knapsack: Unlike 0/1 Knapsack, you can take fractions of an item. This problem can be solved using a greedy approach.
- Bounded Knapsack: Each item has a limited quantity that can be selected.
- Unbounded Knapsack: There are unlimited quantities of each item.
"""

## 7. Trade-offs
"""
- The 0/1 Knapsack algorithm provides an optimal solution but may not be feasible for very large inputs due to its O(nW) space complexity.
- It requires integer weights and capacity, which may not be suitable for problems involving fractional weights or capacities.
"""

## 8. Pitfalls / Gotchas
"""
- Not updating the `dp` array correctly, which can lead to incorrect maximum values.
- Misunderstanding between 0/1 Knapsack and its variants which require different approaches.
- Assuming fractional weights or capacities are supported, which is not the case in the 0/1 Knapsack problem.
"""

## 9. Classic Problems
"""
- The classic 0/1 Knapsack problem itself is a foundational problem in computer science and is often used in teaching dynamic programming concepts.
- Similar patterns are found in problems like subset sum, partition problem, and rod cutting.
"""

## 10. Code Implementation (Demo)
def knapsack_01(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage:
weights = [1, 2, 3, 2]
values = [8, 4, 0, 5]
capacity = 5
max_value = knapsack_01(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)
