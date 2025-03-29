# Unbounded Knapsack Algorithm

```python
```python
# Unbounded Knapsack Algorithm

## 1. Category / Type
"""
Dynamic Programming
"""

## 2. Core Idea / Intuition
"""
The Unbounded Knapsack problem is a variation of the classic Knapsack problem where each item can be chosen multiple times. 
The goal is to maximize the total value in the knapsack without exceeding its capacity, with the ability to use each item 
an unlimited number of times. This is achieved by considering the maximum value obtainable by either including or excluding 
an item repeatedly until the knapsack's capacity is filled.
"""

## 3. Steps / Flow
"""
1. Initialize a list `dp` of size `W + 1` with all zeros, where `W` is the maximum capacity of the knapsack. 
   The `dp[i]` will store the maximum value obtainable with knapsack capacity `i`.

2. Iterate over each capacity `i` from 1 to W:
   - For each item in the given list of items (each with a given weight and value):
     - If the item's weight is less than or equal to the current capacity `i`:
       - Update the `dp[i]` as the maximum of its current value or the value obtained by including the item 
         (i.e., `value_of_item + dp[i - weight_of_item]`).

3. The final value `dp[W]` will contain the maximum value achievable with the full capacity `W`.
"""

## 4. Time & Space Complexity
"""
| Best   | Average | Worst  | Space  |
|--------|---------|--------|--------|
| O(nW)  | O(nW)   | O(nW)  | O(W)   |

- `n` is the number of different items.
- `W` is the maximum capacity of the knapsack.
"""

## 5. Use Cases
"""
- Resource allocation where the same resource can be used multiple times.
- Cutting stock problems in manufacturing.
- Coin change problems where each denomination can be used multiple times.
"""

## 6. Common Variants
"""
- 0/1 Knapsack: Each item can be chosen at most once.
- Fractional Knapsack: Items can be broken into smaller pieces, allowing for fractional selection.
"""

## 7. Trade-offs
"""
- The Unbounded Knapsack allows multiple copies of each item, which can lead to higher memory and processing time 
  compared to the 0/1 Knapsack for large input sizes.
- It is more flexible in applications where resources can be reused or divided indefinitely.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that weights and values are non-negative, as negative values might lead to incorrect calculations.
- Be cautious of integer overflow in languages without automatic large integer handling when weights and values are large.
"""

## 9. Classic Problems
"""
- Coin Change Problem: Finding the minimum number of coins needed to make a certain amount, with unlimited supply of each coin.
- Rod Cutting Problem: Maximizing the profit by cutting a rod into pieces of given lengths and selling them.
"""

## 10. Code Implementation (Demo)
def unbounded_knapsack(W, weights, values):
    # Number of items
    n = len(values)
    
    # Initialize a dp array with zeros
    dp = [0] * (W + 1)
    
    # Iterate over each capacity from 1 to W
    for i in range(1, W + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
    
    return dp[W]

# Example usage:
# W = capacity of the knapsack
# weights = list of weights of items
# values = list of values of items
W = 100
weights = [1, 50]
values = [10, 60]
max_value = unbounded_knapsack(W, weights, values)
print("Maximum value obtainable:", max_value)
```
```