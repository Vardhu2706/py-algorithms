# Huffman Coding Algorithm

```python
```python
# Huffman Coding Algorithm

## 1. Category / Type
"""
Huffman Coding falls under the category of Compression Algorithms, specifically it is a Greedy Algorithm used for lossless data compression.
"""

## 2. Core Idea / Intuition
"""
The core idea behind Huffman Coding is to assign variable-length codes to input characters, with shorter codes assigned to more frequent characters. This results in a prefix-free code (no code is a prefix of any other), which minimizes the total encoded message size.

The algorithm builds a binary tree where each leaf node represents a character from the input data. The path from the root to the leaf node represents the binary code for that character.
"""

## 3. Steps / Flow
"""
1. **Frequency Calculation**:
   - Count the frequency of each character in the input data.

2. **Priority Queue Initialization**:
   - Create a priority queue (usually a min-heap) to hold nodes of the Huffman tree. Each node contains a character and its frequency.

3. **Tree Building**:
   - While there is more than one node in the queue:
     - Extract the two nodes with the smallest frequencies.
     - Create a new internal node with these two nodes as children and a frequency equal to the sum of their frequencies.
     - Insert the new node back into the priority queue.

4. **Code Assignment**:
   - Once the tree is constructed, traverse it from the root to assign codes to each character. Moving left might correspond to appending a '0' and moving right to appending a '1'.

5. **Encoding**:
   - Replace each character in the input data with its corresponding binary code from the tree to get the encoded message.

6. **Decoding**:
   - To decode, traverse the tree using the bits in the encoded message to reach the leaf nodes which represent the characters.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst  | Space  |
|---------|---------|--------|--------|
| O(n log n) | O(n log n) | O(n log n) | O(n)   |

- The time complexity is primarily driven by the operations on the priority queue, which involve inserting and removing nodes.
- Space complexity is O(n) due to the storage of the frequency table and the nodes of the Huffman tree.
"""

## 5. Use Cases
"""
- Data compression, e.g., ZIP file formats.
- Multimedia codecs, e.g., JPEG, MP3.
- Situations where bandwidth or storage is limited and lossless compression is required.
"""

## 6. Common Variants
"""
- Adaptive Huffman Coding: Dynamically adjusts the Huffman tree as the data is being encoded.
- Canonical Huffman Coding: Uses a specific way of assigning codes to ensure compact representation of the tree.
"""

## 7. Trade-offs
"""
- Huffman Coding is optimal for symbol-by-symbol coding with known frequencies, but it may not be optimal for larger block sizes.
- It requires a pass through the data to calculate frequencies, which may not be efficient in streaming scenarios.
- The overhead of storing the Huffman Tree can negate the benefits of compression for small datasets.
"""

## 8. Pitfalls / Gotchas
"""
- Not suitable for very small datasets where the overhead of the Huffman tree outweighs the compression benefits.
- If character frequencies do not vary much, the compression gains might be minimal.
- Managing the priority queue efficiently is crucial for performance.
"""

## 9. Classic Problems
"""
- Encoding and decoding text files with varying character distributions.
- Use in constructing efficient prefix codes for error correction.
"""

## 10. Code Implementation (Demo)
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

import heapq

def calculate_frequencies(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_tree(frequency):
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, current_code="", codes={}):
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_codes(node.left, current_code + "0", codes)
        build_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encoding(data):
    frequency = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequency)
    codes = build_codes(huffman_tree)
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = []
    current_node = huffman_tree
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = huffman_tree

    return ''.join(decoded_data)

# Example usage:
data = "this is an example for huffman encoding"
encoded_data, tree = huffman_encoding(data)
print(f"Encoded: {encoded_data}")
decoded_data = huffman_decoding(encoded_data, tree)
print(f"Decoded: {decoded_data}")
```
```