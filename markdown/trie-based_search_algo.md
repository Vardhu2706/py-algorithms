# Trie-based Search Algorithm

```python
# Trie-based Search Algorithm

## 1. Category / Type
"""
Trie-based Search falls under the category of data structures and searching algorithms.
"""

## 2. Core Idea / Intuition
"""
The core idea of a Trie-based search is to use a tree-like data structure to store a dynamic set of strings, where keys are usually strings. Tries provide fast insert, search, and delete operations for strings by breaking down each string into its individual characters and storing them as nodes in a tree structure. This allows for efficient retrieval operations, making them suitable for autocomplete and spell-checking applications.
"""

## 3. Steps / Flow
"""
1. **Insert Operation:**
   - Start at the root node.
   - For each character in the input string, check if there is a corresponding child node.
   - If a child node exists, move to that node; otherwise, create a new node and move to it.
   - Mark the last node as the end of a word once all characters in the string have been processed.

2. **Search Operation:**
   - Start at the root node.
   - For each character in the query string, check for a corresponding child node.
   - If any character's node is missing, the search fails.
   - If all characters are found and the last node is marked as the end of a word, the search succeeds.

3. **Delete Operation (Optional):**
   - Begin at the root node.
   - Traverse nodes corresponding to the word to be deleted.
   - If the word exists, unmark the last node.
   - Optionally, remove nodes that are no longer necessary.

4. **Autocomplete Operation:**
   - Find the node corresponding to the last character of the prefix.
   - Perform a depth-first search from this node to collect all words that share the prefix.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space         |
|---------|---------|---------|---------------|
| O(m)    | O(m)    | O(m)    | O(n * l)      |

- **m** is the length of the input string.
- **n** is the number of keys in the trie.
- **l** is the average length of the keys.
- The space complexity accounts for storing each character of every input string.
"""

## 5. Use Cases
"""
- **Autocomplete and Autocorrect**: Tries are ideal for suggesting possible completions of a prefix.
- **Spell Checking**: Tries can quickly validate if a word exists in a dictionary.
- **IP Routing**: Tries can be used in network routers to store routing tables.
- **Longest Prefix Matching**: Useful in implementing algorithms that require prefix-based searching.
"""

## 6. Common Variants
"""
- **Compressed Trie**: Reduces redundant nodes by merging chains of single-child nodes.
- **Suffix Trie**: Used for fast substring searching within a single text.
- **Patricia Trie**: A compact form of the trie that combines paths of single-child nodes.
"""

## 7. Trade-offs
"""
- **Memory Usage**: Tries can consume more memory compared to hash tables, especially for sparse data.
- **Complexity**: Implementing a trie is more complex than simpler data structures like arrays or linked lists.
- **Insertion Performance**: While tries offer fast search times, they can be slower to insert compared to hash tables.
"""

## 8. Pitfalls / Gotchas
"""
- **Space Complexity**: Poorly implemented tries can lead to excessive memory usage.
- **Character Set**: The trie needs to handle the full range of possible characters, which can be challenging when working with large or Unicode character sets.
- **Deletion Complexity**: Deleting words can be tricky, especially when maintaining the compactness of the trie.
"""

## 9. Classic Problems
"""
- **Autocomplete Feature**: Implementing search engines or text editors that predict user input.
- **Dictionary Word Search**: Efficiently finding words in a dictionary application.
- **IP Address Routing**: Storing and searching routing paths in networking applications.
"""

## 10. Code Implementation (Demo)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix: str):
        def dfs(current_node, path, results):
            if current_node.is_end_of_word:
                results.append(''.join(path))
            for char, next_node in current_node.children.items():
                path.append(char)
                dfs(next_node, path, results)
                path.pop()

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        dfs(node, list(prefix), results)
        return results
```