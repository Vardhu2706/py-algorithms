# Edit Distance Algorithm

## 1. Category / Type
"""
Dynamic Programming
"""

## 2. Core Idea / Intuition
"""
The Edit Distance algorithm, also known as Levenshtein Distance, aims to find the minimum number of operations required to convert one string into another. The allowable operations include insertion, deletion, and substitution of a single character. The core idea is to use a dynamic programming approach to build a solution incrementally by solving smaller subproblems.

The intuition behind this algorithm is to construct a 2D table where each cell (i, j) represents the edit distance between the first i characters of one string and the first j characters of the other string. By systematically building up solutions to these smaller subproblems, we can derive the solution to the entire problem.
"""

## 3. Steps / Flow
"""
1. **Initialize a DP Table:**
   - Create a 2D array `dp` where `dp[i][j]` will store the edit distance between the first `i` characters of `s1` and the first `j` characters of `s2`.
   - The dimensions of the table will be `(len(s1)+1) x (len(s2)+1)`.

2. **Base Case Initialization:**
   - If one string is empty, the edit distance is the length of the other string.
   - Initialize `dp[i][0] = i` for all `i` and `dp[0][j] = j` for all `j`.

3. **Fill the DP Table:**
   - Iterate over each character in `s1` and `s2`.
   - For each pair of indices `(i, j)`, determine if the characters `s1[i-1]` and `s2[j-1]` are the same.
   - If they are the same, then `dp[i][j] = dp[i-1][j-1]`.
   - If they are not the same, calculate the minimum edit distance by considering:
     - Insertion: `dp[i][j-1] + 1`
     - Deletion: `dp[i-1][j] + 1`
     - Substitution: `dp[i-1][j-1] + 1`
   - Set `dp[i][j]` to the minimum of these values.

4. **Return the Result:**
   - The edit distance between the entire strings `s1` and `s2` is found at `dp[len(s1)][len(s2)]`.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(m*n) | O(m*n) | O(m*n) | O(m*n) |
Where `m` is the length of the first string and `n` is the length of the second string. The complexities account for filling a 2D table of size `m+1 x n+1`.
"""

## 5. Use Cases
"""
- DNA sequence analysis to find how similar two sequences are.
- Spell-checking algorithms to suggest corrections.
- Natural Language Processing (NLP) tasks like text similarity.
- Data de-duplication and record linkage.
"""

## 6. Common Variants
"""
- **Damerau-Levenshtein Distance:** Considers transpositions along with insertion, deletion, and substitution.
- **Hamming Distance:** Measures the number of positions at which the corresponding symbols are different, applicable when strings are of equal length.
"""

## 7. Trade-offs
"""
- The algorithm's time and space complexity can be limiting for very large strings due to the quadratic growth of the DP table.
- While dynamic programming provides an optimal solution in terms of minimizing operations, it does not capture contextual or semantic similarity.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure proper initialization of the DP table to handle base cases accurately.
- Be cautious with the indices when accessing the strings and the DP table, as off-by-one errors are common.
- The algorithm assumes equal cost for all operations, which may not always be suitable for all applications.
"""

## 9. Classic Problems
"""
- Finding the minimum edit distance is a classic problem in string processing and is often used in competitive programming and coding interviews.
"""

## 10. Code Implementation (Demo)
def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    return dp[m][n]
