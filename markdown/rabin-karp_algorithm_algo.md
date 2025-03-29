# Rabin-Karp Algorithm Algorithm

```python
```python
# Rabin-Karp Algorithm

## 1. Category / Type
"""
The Rabin-Karp Algorithm belongs to the category of string searching algorithms.
It is specifically used for substring search within a larger text.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Rabin-Karp algorithm is to use hashing to find any one of a set of pattern strings in a text.
It computes a hash value for the pattern and each substring of the text of the same length as the pattern.
By comparing hash values, it can quickly identify potential matches. If a hash match is found, the actual strings are compared to avoid false positives due to hash collisions.
"""

## 3. Steps / Flow
"""
1. Compute the hash value of the pattern string (P).
2. Compute the hash value of the first window of the text (T) of the same length as the pattern.
3. Slide the window over the text one character at a time and update the hash value of the current window.
4. For each window:
   - Compare the hash value of the window with the hash value of the pattern.
   - If the hash values match, perform a character-by-character comparison to confirm a match.
5. If a match is confirmed, record the starting index.
6. Continue until the text is fully processed.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst       | Space |
|---------|---------|-------------|-------|
| O(n+m)  | O(n+m)  | O(n*m) (*)  | O(1)  |

(*) In the worst case, the Rabin-Karp algorithm may degenerate into a O(n*m) complexity when hash collisions are frequent, causing every hash match to require a full substring comparison.
"""

## 5. Use Cases
"""
- Searching for a pattern in a large body of text.
- Useful in plagiarism detection where multiple patterns need to be searched simultaneously.
- DNA sequence analysis.
"""

## 6. Common Variants
"""
- Rolling hash improvements for faster hash computation.
- Multi-pattern Rabin-Karp where multiple patterns are searched simultaneously.
"""

## 7. Trade-offs
"""
- The choice of hash function affects the performance; a poor hash function may lead to frequent collisions.
- Although average case complexity is efficient, the algorithm can degrade to O(n*m) in the worst case.
- Requires careful handling of large numbers during hash computation to avoid integer overflow.
"""

## 8. Pitfalls / Gotchas
"""
- Hash collisions: A hash collision does not guarantee a match and requires direct string comparison.
- Handling of hash values: Care must be taken to ensure hash values are computed accurately, especially in modular arithmetic.
"""

## 9. Classic Problems
"""
- Detecting plagiarism by checking for matching substrings across documents.
- Implementing spell-checkers that detect similar patterns.
"""

## 10. Code Implementation (Demo)
def rabin_karp(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    pattern_hash = 0
    current_window_hash = 0
    h = 1
    result = []

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m-1):
        h = (h * 256) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        current_window_hash = (256 * current_window_hash + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        if pattern_hash == current_window_hash:
            # If the hash values match, then only check for characters one by one
            if text[i:i + m] == pattern:
                result.append(i)

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n - m:
            current_window_hash = (256 * (current_window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # We might get negative value of t, converting it to positive
            if current_window_hash < 0:
                current_window_hash = current_window_hash + prime

    return result

# Example usage:
# text = "GEEKS FOR GEEKS"
# pattern = "GEEK"
# print(rabin_karp(text, pattern))  # Output: [0, 10]
```
```