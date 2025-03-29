# Union-Find (Disjoint Set Union) Algorithm

```python
```python
# Union-Find (Disjoint Set Union) Algorithm

## 1. Category / Type
"""
Graph Theory / Data Structures
"""

## 2. Core Idea / Intuition
"""
The Union-Find algorithm, also known as Disjoint Set Union (DSU), is a data structure that manages a partition of a set into disjoint (non-overlapping) subsets. It provides near-constant time operations to:
- Find the representative (or "root") of the subset a particular element is in.
- Union two subsets into a single subset.

The core idea is to use two main operations:
- Find: Determine which subset a particular element is in. This can be used to determine if two elements are in the same subset.
- Union: Join two subsets into a single subset.

The efficiency of these operations is improved using two techniques:
- Path Compression: During the find operation, we make the tree flat, so that all nodes directly point to the root.
- Union by Rank: We always attach the smaller tree under the root of the larger tree.
"""

## 3. Steps / Flow
"""
1. **Initialization**: Create a list where each element is its own parent, representing individual subsets.
2. **Find Operation**:
   - Recursively find the root of the element.
   - Apply path compression by making each node on the path point directly to the root.
3. **Union Operation**:
   - Use the find operation to determine the roots of the subsets containing the two elements.
   - Attach one root to the other based on the rank (size) of each tree.
   - Update the rank if both trees have the same rank.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space  |
|---------|---------|---------|--------|
| O(α(n)) | O(α(n)) | O(α(n)) | O(n)   |

- α(n) is the Inverse Ackermann function, which grows very slowly, making the operations nearly constant time.
"""

## 5. Use Cases
"""
- Network connectivity: Determine if there is a path between two nodes.
- Kruskal's Minimum Spanning Tree algorithm.
- Image processing for finding connected components.
- Dynamic connectivity problems.
"""

## 6. Common Variants
"""
- Weighted Quick Union: Uses union by size to keep the tree flat.
- Quick Union: A simpler variant without path compression, leading to potentially taller trees.
"""

## 7. Trade-offs
"""
- The trade-off between simplicity and efficiency: The basic Quick Union is easier to implement but less efficient without path compression and rank.
- Memory usage: Storing additional information like rank increases memory usage.
"""

## 8. Pitfalls / Gotchas
"""
- Not implementing path compression or union by rank can lead to inefficient trees, resulting in O(n) time complexity for operations.
- Incorrectly updating the rank during union operations can lead to incorrect tree structures.
"""

## 9. Classic Problems
"""
- Dynamic connectivity in graphs.
- Determining connected components in undirected graphs.
- Percolation problem in statistical mechanics.
"""

## 10. Code Implementation (Demo)
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
```
```