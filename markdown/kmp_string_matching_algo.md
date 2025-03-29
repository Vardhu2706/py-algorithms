# KMP String Matching Algorithm

```python
# KMP String Matching Algorithm

## 1. Category / Type
"""
- String Matching
- Pattern Searching
"""

## 2. Core Idea / Intuition
"""
The Knuth-Morris-Pratt (KMP) algorithm is a linear time string matching algorithm that seeks to find occurrences of a "pattern" string within a "text" string. The primary innovation of KMP is the construction of a partial match table (also known as the "longest prefix suffix" or LPS array), which allows the algorithm to avoid unnecessary comparisons by skipping over sections of the text that have already been matched.

The algorithm operates in two main phases:
1. Preprocessing Phase: Construct the LPS array for the pattern, which will be used during the search phase to decide how many characters can be skipped.
2. Searching Phase: Use the LPS array to efficiently search for the pattern within the text.
"""

## 3. Steps / Flow
"""
1. **Preprocess the Pattern to Create the LPS Array:**
   - Initialize an LPS array of the same length as the pattern with all values set to 0.
   - Use two pointers, `length` and `i`, to traverse the pattern and calculate the longest prefix which is also a suffix.
   - If characters match, increment the `length` and set `lps[i] = length`, then move to the next character (`i++`).
   - If they do not match and `length` is not zero, set `length = lps[length - 1]`. Otherwise, set `lps[i] = 0` and move to the next character.

2. **Search the Pattern in the Text:**
   - Use two pointers, `i` for the text and `j` for the pattern.
   - Compare characters of the text and pattern.
   - If characters match, increment both `i` and `j`.
   - If `j` reaches the end of the pattern, it means the pattern is found. Reset `j` using `lps[j-1]` and continue.
   - If characters do not match, and `j` is not zero, reset `j` using `lps[j-1]`. If `j` is zero, increment `i`.

This use of the LPS array ensures that the algorithm does not backtrack over characters in the text, leading to an efficient solution.
"""

## 4. Time & Space Complexity
"""
| Best   | Average | Worst  | Space |
|--------|---------|--------|-------|
| O(n)   | O(n)    | O(n)   | O(m)  |

- `n` is the length of the text.
- `m` is the length of the pattern.
- The time complexity is linear in all cases due to the efficient skipping mechanism provided by the LPS array.
- The space complexity is linear with respect to the pattern size due to the LPS array.
"""

## 5. Use Cases
"""
- Finding a substring within a larger string.
- Search functionalities in text editors.
- DNA sequence analysis, where specific patterns need to be identified in a long sequence.
- Spam filtering, where specific patterns (like keywords) are searched within emails or messages.
"""

## 6. Common Variants
"""
- **Boyer-Moore Algorithm:** Another efficient string matching algorithm that uses the concept of bad character and good suffix heuristics.
- **Rabin-Karp Algorithm:** Uses hashing to find any one of a set of pattern strings in a text.
"""

## 7. Trade-offs
"""
- The KMP algorithm is optimal for scenarios where the text is much larger than the pattern.
- Construction of the LPS array requires additional space and preprocessing time, which may not be ideal for very short patterns.
- In cases where the pattern does not repeat much, simpler algorithms like brute force may be more straightforward to implement.
"""

## 8. Pitfalls / Gotchas
"""
- Incorrect implementation of the LPS array construction can lead to incorrect skipping and hence incorrect results.
- KMP assumes zero-based indexing; off-by-one errors are common when implementing the algorithm.
"""

## 9. Classic Problems
"""
- Searching for a repeated sequence within a string.
- Detecting plagiarism by finding matching phrases in large documents.
- Searching for patterns in log files or other structured data.
"""

## 10. Code Implementation (Demo)

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
```