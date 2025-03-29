# Coin Change Algorithm

## 1. Category / Type
"""
- Dynamic Programming
- Greedy Algorithm (for specific variations)
"""

## 2. Core Idea / Intuition
"""
The core idea of the Coin Change algorithm is to determine the minimum number of coins required to make up a given amount of money from a set of coins with predefined denominations.
The problem can be approached using dynamic programming by finding the optimal solution for smaller subproblems and building up to the solution for the main problem.
The key intuition is to minimize the number of coins by considering each coin's contribution and recursively solving the subproblems.
"""

## 3. Steps / Flow
"""
1. Initialize a list `dp` of size `amount + 1` with all elements set to `amount + 1`, except for `dp[0]` which is set to 0. This list will store the minimum number of coins needed for each amount from 0 to the target amount.
2. Iterate over each amount `i` from 1 to the `amount`.
   - For each coin in the list of coins:
     - If the coin's denomination is less than or equal to `i`, update `dp[i]` to be the minimum of `dp[i]` and `dp[i - coin] + 1`.
3. After filling in the `dp` list, check `dp[amount]`:
   - If it is greater than `amount`, return -1 indicating it's not possible to make the given amount with the available coins.
   - Otherwise, return `dp[amount]` as the minimum number of coins required.
"""

## 4. Time & Space Complexity
"""
| Best   | Average | Worst  | Space  |
|--------|---------|--------|--------|
| O(n)   | O(n*m)  | O(n*m) | O(n)   |

- `n` is the amount to be formed.
- `m` is the number of different coin denominations.
- Time complexity is primarily determined by the nested loop over the amount and the coins.
- Space complexity is O(n) because of the `dp` array used to store results for each subproblem.
"""

## 5. Use Cases
"""
- Financial applications where change needs to be given efficiently.
- Resource allocation problems where discrete units need to be distributed optimally.
- Game development for currency systems within games.
"""

## 6. Common Variants
"""
- Coin Change Problem with exact denomination requirement.
- Minimizing the number of coins for an exact change using a limited number of each coin type.
- Maximizing the number of ways to make change for a given amount.
"""

## 7. Trade-offs
"""
- The dynamic programming approach uses more memory but generally runs faster than a naive recursive solution.
- Greedy algorithms may provide faster solutions in specific cases but can fail for certain denominations.
- Time complexity increases with the number of denominations and the amount, making it less suitable for very large inputs without optimization.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure the coin denominations are positive integers.
- Watch for off-by-one errors in index calculations, especially in the initialization of the `dp` list.
- Be cautious of integer overflow in languages that don't automatically handle large integers.
"""

## 9. Classic Problems
"""
- The classic "Knapsack Problem" shares similarities in terms of dynamic programming techniques.
- Making change with unlimited supply of coins, a well-known problem in combinatorics.
"""

## 10. Code Implementation (Demo)
def coin_change(coins, amount):
    # Initialize the dp array with a default value greater than any possible answer
    dp = [amount + 1] * (amount + 1)
    # Base case: zero amount requires zero coins
    dp[0] = 0
    
    # Loop through each amount from 1 to the target amount
    for i in range(1, amount + 1):
        # Check each coin
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= i:
                # Update the dp value for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still the default value, return -1 to indicate impossibility
    return dp[amount] if dp[amount] <= amount else -1

# Example usage:
# coins = [1, 2, 5]
# amount = 11
# print(coin_change(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)
