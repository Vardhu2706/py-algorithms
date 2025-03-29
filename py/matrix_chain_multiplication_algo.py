# Matrix Chain Multiplication Algorithm

## 1. Category / Type
"""
Dynamic Programming
"""

## 2. Core Idea / Intuition
"""
The Matrix Chain Multiplication problem aims to determine the most efficient way to multiply a given sequence of matrices. The goal is to minimize the total number of scalar multiplications needed. This is achieved by deciding the order in which the matrices are multiplied, as matrix multiplication is associative but not commutative. The problem can be solved using dynamic programming by breaking it down into simpler subproblems, where each subproblem involves calculating the minimum cost for a specific sequence of matrix multiplications.
"""

## 3. Steps / Flow
"""
1. **Define Subproblems**: Let m[i][j] represent the minimum number of scalar multiplications needed to compute the product of matrices Ai through Aj.

2. **Initialization**: 
   - For each matrix Ai, set m[i][i] = 0 because the cost of multiplying one matrix is zero.

3. **Recursive Relation**:
   - For chain lengths l from 2 to n:
     - For each i from 1 to n-l+1:
       - Set j = i+l-1
       - Set m[i][j] to an infinitely large number initially.
       - For each k from i to j-1:
         - Compute q = m[i][k] + m[k+1][j] + cost of multiplying Ai...Ak and Ak+1...Aj
         - Update m[i][j] if q is smaller than the current m[i][j].

4. **Compute and Return Result**:
   - The final result is stored in m[1][n], which gives the minimum cost to multiply the entire chain.
"""

## 4. Time & Space Complexity
"""
| Best       | Average   | Worst     | Space     |
|------------|-----------|-----------|-----------|
| O(n^3)     | O(n^3)    | O(n^3)    | O(n^2)    |
"""

## 5. Use Cases
"""
- Optimizing the performance of algorithms involving multiple matrix operations.
- Applications in computer graphics and machine learning where matrix operations are frequent.
- Database query optimization, where relational algebra operations can be optimized.
"""

## 6. Common Variants
"""
- The Parenthesization Problem: Determining the actual sequence of matrix multiplications.
- Weighted Matrix Chain Multiplication: Incorporating weights or costs associated with each matrix.
"""

## 7. Trade-offs
"""
- Space Complexity: The algorithm requires O(n^2) space, which can be limiting for very large sequences of matrices.
- Preprocessing Time: Despite its efficiency, the preprocessing step involves O(n^3) computations, which can be substantial for large n.
"""

## 8. Pitfalls / Gotchas
"""
- Incorrect Initialization: Failure to initialize the m[i][i] entries to zero can lead to incorrect results.
- Misplaced Indices: Off-by-one errors are common when iterating over matrix dimensions.
- Not considering the cost of individual matrix dimensions properly can lead to miscalculations.
"""

## 9. Classic Problems
"""
- Determining the optimal order of operations in computational tasks.
- Evaluating complex expressions in symbolic computation.
- Sequence alignment in bioinformatics.
"""

## 10. Code Implementation (Demo)
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[1][n]

# Example usage:
p = [30, 35, 15, 5, 10, 20, 25]
print("Minimum number of multiplications is", matrix_chain_order(p))
