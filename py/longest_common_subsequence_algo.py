# Longest Common Subsequence Algorithm

## 1. Category / Type
"""
The Longest Common Subsequence (LCS) algorithm belongs to the category of Dynamic Programming.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Longest Common Subsequence problem is to determine the longest subsequence that is common to two sequences. A subsequence is a sequence derived from another sequence where some elements may be deleted without changing the order of the remaining elements.

The intuition behind using dynamic programming for LCS is to build a solution to the problem incrementally by solving smaller subproblems first and using their solutions to solve larger problems. This avoids redundant calculations and reduces the computational complexity compared to a naive recursive approach.
"""

## 3. Steps / Flow
"""
1. Initialize a 2D array `dp` where `dp[i][j]` will hold the length of the longest common subsequence of the first `i` characters of the first string and the first `j` characters of the second string.

2. Set the first row and first column of the `dp` table to 0, representing the base case where one of the strings is empty.

3. Iterate through each character of both strings using two nested loops:
   - If the characters match (`str1[i-1] == str2[j-1]`), set `dp[i][j] = dp[i-1][j-1] + 1`.
   - If the characters do not match, set `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

4. After filling up the `dp` table, the bottom-right cell (`dp[len(str1)][len(str2)]`) contains the length of the longest common subsequence.

5. Optionally, backtrack from `dp[len(str1)][len(str2)]` to reconstruct the LCS itself.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(n*m) | O(n*m) | O(n*m) | O(n*m) |

Where `n` and `m` are the lengths of the two strings. The complexity is dominated by the double loop over the input strings, and the space complexity is due to storing the `dp` table.
"""

## 5. Use Cases
"""
- Comparing DNA sequences in bioinformatics.
- Version control systems for diff operations.
- Finding similarities between text files or documents.
"""

## 6. Common Variants
"""
- Longest Common Substring: Looks for the longest contiguous segment that is common to both strings.
- Shortest Common Supersequence: Finds the shortest sequence containing both strings as subsequences.
- Edit Distance: Measures the minimum number of edit operations to transform one string into another.
"""

## 7. Trade-offs
"""
- Using a full 2D `dp` table is straightforward but can be memory-intensive for very long strings.
- Space can be optimized to O(min(n, m)) by using two arrays to store only the previous and current rows of the `dp` table.
"""

## 8. Pitfalls / Gotchas
"""
- Confusing substring with subsequence: Subsequence allows for non-contiguous characters, while substring does not.
- Off-by-one errors: Care must be taken with indices, especially when initializing the `dp` table and accessing string characters.
"""

## 9. Classic Problems
"""
- Longest Increasing Subsequence: A variation where the subsequence must be strictly increasing.
- Sequence Alignment: Extends LCS with penalties for mismatches and gaps, used extensively in bioinformatics.
"""

## 10. Code Implementation (Demo)
def longest_common_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Optional: reconstruct the LCS string
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    
    return dp[n][m], ''.join(lcs)

# Example usage:
# str1 = "ABCBDAB"
# str2 = "BDCAB"
# length, lcs_string = longest_common_subsequence(str1, str2)
# print("Length of LCS:", length)
# print("LCS:", lcs_string)
