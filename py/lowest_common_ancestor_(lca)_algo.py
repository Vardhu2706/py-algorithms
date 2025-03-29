# Lowest Common Ancestor (LCA) Algorithm

## 1. Category / Type
"""
The Lowest Common Ancestor (LCA) algorithm falls under the category of Tree Algorithms. It is particularly associated with Binary Trees and Binary Search Trees (BSTs).
"""

## 2. Core Idea / Intuition
"""
The core idea of the LCA algorithm is to find the lowest (i.e., deepest) node in a tree that is an ancestor of two given nodes. This is crucial in scenarios where we need to determine a common root or base for two nodes in hierarchical data structures like trees.
"""

## 3. Steps / Flow
"""
1. **Binary Tree Approach**:
   - Start from the root and traverse the tree.
   - If the current node is either of the two nodes for which LCA is being determined, return the current node.
   - Recursively look for the nodes in the left and right subtrees.
   - If both calls return non-null values, the current node is the LCA.
   - Otherwise, return the non-null value obtained from either the left or right subtree.

2. **Binary Search Tree (BST) Approach**:
   - Utilize the properties of BST where left children are lesser and right children are greater.
   - Start from the root.
   - If both nodes are smaller than the current node, LCA lies in the left subtree.
   - If both nodes are greater than the current node, LCA lies in the right subtree.
   - If one node is on the left and the other is on the right, the current node is the LCA.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space    |
|-----------|-----------|-----------|----------|
| O(log n)  | O(n)      | O(n)      | O(h)     |

- Here, `n` is the number of nodes in the tree and `h` is the height of the tree.
- In a balanced BST, the complexity can be O(log n), while in a skewed tree, it can degrade to O(n).
- Space complexity is O(h) due to recursion stack, where `h` is the height of the tree.
"""

## 5. Use Cases
"""
- Finding the relationship between two nodes in a hierarchy.
- Used in file systems and version control systems to determine common ancestors.
- Applications in network routing to find common routers or switches.
"""

## 6. Common Variants
"""
- LCA in Binary Trees.
- LCA in Binary Search Trees (BSTs).
- LCA in Directed Acyclic Graphs (DAGs) using different algorithms like Tarjan's offline LCA algorithm.
"""

## 7. Trade-offs
"""
- While the LCA algorithm is efficient for balanced trees, it can be less efficient for unbalanced trees.
- For dynamic trees, where nodes are frequently added or removed, additional data structures like parent pointers or Euler tours may be required for efficient LCA computation.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure the nodes for which LCA is being found are present in the tree.
- In a BST, do not incorrectly assume that the property of BST simplifies the problem without considering node values.
- Be cautious with edge cases like one node being an ancestor of the other.
"""

## 9. Classic Problems
"""
- Finding the LCA of nodes in a family tree.
- Determining the closest shared directory in a file system hierarchy.
- Finding intersections in network paths.
"""

## 10. Code Implementation (Demo)
def find_lca(root, n1, n2):
    # Base case
    if root is None:
        return None
    
    # If either n1 or n2 matches with root, report the presence by returning root
    if root.data == n1 or root.data == n2:
        return root
    
    # Look for keys in left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    
    # If both left_lca and right_lca are non-NULL, then one key is present in one subtree and the other is present in the other subtree. So this node is the LCA
    if left_lca and right_lca:
        return root
    
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca else right_lca
