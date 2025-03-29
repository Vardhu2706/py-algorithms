# Binary Tree Traversals Algorithm

```python
# Binary Tree Traversals Algorithm

## 1. Category / Type
"""
- Tree Traversal
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
"""

## 2. Core Idea / Intuition
"""
Binary Tree Traversals are methods of visiting all the nodes in a binary tree systematically. The primary goal is to ensure that each node is processed in a specific order. There are several types of traversals, each serving different purposes:

1. **In-order Traversal**: Visit the left subtree, the root node, and then the right subtree.
2. **Pre-order Traversal**: Visit the root node, the left subtree, and then the right subtree.
3. **Post-order Traversal**: Visit the left subtree, the right subtree, and then the root node.
4. **Level-order Traversal**: Visit nodes level by level from the root.

Each traversal method provides unique insights into the tree's structure and can be applied to solve different computational problems like searching, sorting, and manipulating hierarchical data.
"""

## 3. Steps / Flow
"""
### In-order Traversal
1. Recursively traverse the left subtree.
2. Process the root node.
3. Recursively traverse the right subtree.

### Pre-order Traversal
1. Process the root node.
2. Recursively traverse the left subtree.
3. Recursively traverse the right subtree.

### Post-order Traversal
1. Recursively traverse the left subtree.
2. Recursively traverse the right subtree.
3. Process the root node.

### Level-order Traversal
1. Utilize a queue to track nodes at the current level.
2. Start from the root node.
3. Process each node, and enqueue its children.
4. Repeat until all nodes are processed.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(n) | O(n)    | O(n)  | O(h)  |

Where `n` is the number of nodes in the tree, and `h` is the height of the tree. The space complexity for DFS traversals is O(h) due to the recursion stack, whereas for BFS (level-order traversal), it is O(w), where `w` is the maximum width of the tree.
"""

## 5. Use Cases
"""
- **In-order Traversal**: Commonly used in binary search trees to retrieve nodes in a sorted order.
- **Pre-order Traversal**: Useful for creating a copy of the tree and prefix expression evaluations.
- **Post-order Traversal**: Useful for deleting the tree and postfix expression evaluations.
- **Level-order Traversal**: Used in algorithms like breadth-first search, and is useful for finding the shortest path on unweighted graphs.
"""

## 6. Common Variants
"""
- **Reverse In-order Traversal**: Right, Root, Left; used for descending order retrieval in binary search trees.
- **Zigzag Level-order Traversal**: Traversal that visits nodes in a zigzag pattern level by level.
"""

## 7. Trade-offs
"""
- **In-order, Pre-order, Post-order** require O(h) space for the recursion stack, which can be inefficient for very deep trees.
- **Level-order** can become inefficient in terms of space complexity due to the queue storing all nodes at a level, especially for wide trees.
"""

## 8. Pitfalls / Gotchas
"""
- Recursive implementations can lead to stack overflow for very deep trees; iterative versions can overcome this issue.
- Ensure that null (None in Python) checks are in place to avoid dereferencing errors.
"""

## 9. Classic Problems
"""
- **Tree Traversal Problems**: Finding the depth of the tree, checking if two trees are identical, flattening a tree to a linked list.
- **Expression Tree Evaluations**: Using traversals to evaluate arithmetic expressions.
"""

## 10. Code Implementation (Demo)
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

def post_order_traversal(root):
    if root is None:
        return []
    return post_order_traversal(root.left) + post_order_traversal(root.right) + [root.value]

from collections import deque

def level_order_traversal(root):
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```
```