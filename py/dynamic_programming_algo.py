# Dynamic Programming Algorithm

## 1. Category / Type
"""
Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure.
"""

## 2. Core Idea / Intuition
"""
The core idea of Dynamic Programming (DP) is to solve each subproblem only once and store its solution in a table, thereby avoiding the overhead of recomputing the solution every time the subproblem is encountered. This approach is particularly useful for optimization problems, where the goal is to find the best solution among many possible solutions.

DP can be implemented in two main ways:
- **Top-Down Approach (Memoization):** This involves solving the problem recursively and storing the results of subproblems in a table to avoid redundant calculations.
- **Bottom-Up Approach (Tabulation):** This involves solving smaller subproblems first and using their solutions to build up the solution to the original problem.
"""

## 3. Steps / Flow
"""
1. **Define the Subproblems:**
   - Identify the subproblems and how they relate to the original problem.

2. **Characterize the Structure of an Optimal Solution:**
   - Determine a recursive formula that relates the solution of the subproblems to the solution of the original problem.

3. **Implement a Recursive Solution (Top-Down) or Iterative Solution (Bottom-Up):**
   - For Top-Down: Implement a recursive function that uses memoization to cache results.
   - For Bottom-Up: Create a table to store the solutions to subproblems and fill it iteratively.

4. **Compute the Value of the Optimal Solution:**
   - Use the recursive formula or the filled table to compute the solution to the original problem.

5. **Construct the Optimal Solution (if necessary):**
   - If the problem requires not just the value of the optimal solution but the solution itself, trace back through the table to construct the solution.
"""

## 4. Time & Space Complexity
"""
| Best     | Average | Worst    | Space     |
|----------|---------|----------|-----------|
| O(n^2)   | O(n^2)  | O(n^2)   | O(n) or O(n^2) depending on problem |
"""

## 5. Use Cases
"""
Dynamic Programming is used in a wide range of applications, including:
- **Optimization Problems:** Such as the Knapsack problem, where the goal is to maximize or minimize some value.
- **Combinatorial Problems:** Such as counting the number of ways to arrange or select items.
- **Sequence Alignment:** Used in bioinformatics to align DNA sequences.
- **Graph Algorithms:** Such as finding the shortest path (e.g., Floyd-Warshall algorithm).
"""

## 6. Common Variants
"""
- **Memoization (Top-Down):** Caching results of expensive function calls and returning the cached result when the same inputs occur again.
- **Tabulation (Bottom-Up):** Building a table iteratively from base cases up to the desired solution.
- **Space Optimization Techniques:** Reducing space complexity by using only necessary space, such as using two rows or even one row for computation.
"""

## 7. Trade-offs
"""
- **Time vs Space:** Dynamic Programming often trades increased space complexity for reduced time complexity.
- **Implementation Complexity:** While powerful, DP solutions can be more complex to implement and require careful consideration of base cases and transition equations.
- **Scalability:** DP solutions can be limited by available memory, especially for large input sizes.
"""

## 8. Pitfalls / Gotchas
"""
- **Incorrect Subproblem Definition:** Misidentifying subproblems can lead to incorrect solutions.
- **Overlapping Subproblem Assumption:** Not all problems with optimal substructure have overlapping subproblems, making DP inapplicable.
- **Memory Limitations:** Large DP tables can lead to high memory usage, potentially causing out-of-memory errors.
"""

## 9. Classic Problems
"""
- **Fibonacci Sequence:** Calculating Fibonacci numbers efficiently.
- **Knapsack Problem:** Solving the 0/1 Knapsack problem using DP.
- **Longest Common Subsequence (LCS):** Finding the longest subsequence present in two sequences.
- **Edit Distance:** Calculating the minimum number of operations to convert one string into another.
- **Coin Change Problem:** Finding the minimum number of coins needed to make a certain amount.
"""

## 10. Code Implementation (Demo)
def fibonacci(n, memo={}):
    """
    Computes the nth Fibonacci number using memoization (Top-Down Dynamic Programming).
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    memo (dict): A dictionary to store computed Fibonacci numbers.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example usage
print(fibonacci(10))  # Output: 55
