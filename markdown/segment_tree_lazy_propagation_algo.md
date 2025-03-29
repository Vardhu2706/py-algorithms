# Segment Tree Lazy Propagation Algorithm

```python
```python
# Segment Tree Lazy Propagation Algorithm

## 1. Category / Type
"""
Segment Tree with Lazy Propagation is a data structure used for efficient range queries and updates.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Segment Tree with Lazy Propagation is to optimize update operations by deferring or "lazily" updating segments of the tree until absolutely necessary. This approach is particularly useful when there are multiple updates to overlapping segments. Instead of updating each segment immediately, the updates are recorded and propagated down the tree only when needed, such as during a query or when the affected node must be processed.
"""

## 3. Steps / Flow
"""
1. **Initialization**: 
   - Construct a segment tree for a given array where each node represents a segment or a range of the data.
   - Create a lazy array of the same size as the segment tree to store the deferred updates.

2. **Build the Tree**:
   - Recursively divide the array into two halves until each segment contains a single element.
   - Store computed values (e.g., sum, minimum, maximum) at each node for its segment.

3. **Update Operation with Lazy Propagation**:
   - To update a range, mark the node with the update value in the lazy array.
   - Instead of immediately updating child nodes, defer this update using the lazy array.
   - Propagate the lazy update only when the affected segment is queried or updated further.

4. **Query Operation**:
   - Check for any pending updates in the lazy array and apply them before returning the result.
   - Recursively collect results from relevant child nodes, considering deferred updates.

5. **Propagation**:
   - Apply and propagate updates from the lazy array to ensure the segment tree reflects the latest changes when necessary.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst  | Space |
|---------|---------|--------|-------|
| O(log n)| O(log n)| O(log n)| O(n)  |
"""

## 5. Use Cases
"""
- Efficiently handling range sum queries and updates in an array.
- Problems involving range minimum/maximum queries with updates.
- Applications in computational geometry, database systems, and more where range query efficiency is crucial.
"""

## 6. Common Variants
"""
- Persistent Segment Tree: Allows access to previous versions of the array.
- Dynamic Segment Tree: Allows the segment tree to handle dynamic size or range changes.
- 2D Segment Tree: Extends the concept to two-dimensional data for range queries in matrices.
"""

## 7. Trade-offs
"""
- Increased complexity compared to a simple segment tree due to lazy propagation mechanisms.
- Higher memory usage due to additional lazy array.
- Suitable for static data ranges; less efficient for dynamic data where size changes frequently.
"""

## 8. Pitfalls / Gotchas
"""
- Incorrect lazy propagation can lead to stale or incorrect query results.
- Mismanagement of the lazy array can result in excessive memory usage or performance degradation.
- Off-by-one errors are common when dealing with indices in recursive functions.
"""

## 9. Classic Problems
"""
- Range Sum Queries with Updates: Given an array, efficiently process multiple sum queries and range update operations.
- Range Minimum/Maximum Queries with Updates: Similar to sum queries but focuses on finding minimum or maximum values.
"""

## 10. Code Implementation (Demo)
class SegmentTreeLazy:
    def __init__(self, data):
        n = len(data)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(data, 0, 0, n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self.build(data, left, start, mid)
            self.build(data, right, mid + 1, end)
            self.tree[node] = self.tree[left] + self.tree[right]

    def update_range(self, l, r, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                left = 2 * node + 1
                right = 2 * node + 2
                self.lazy[left] += self.lazy[node]
                self.lazy[right] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                left = 2 * node + 1
                right = 2 * node + 2
                self.lazy[left] += val
                self.lazy[right] += val
            return

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        self.update_range(l, r, val, left, start, mid)
        self.update_range(l, r, val, right, mid + 1, end)
        self.tree[node] = self.tree[left] + self.tree[right]

    def query_range(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if start > end or start > r or end < l:
            return 0

        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                left = 2 * node + 1
                right = 2 * node + 2
                self.lazy[left] += self.lazy[node]
                self.lazy[right] += self.lazy[node]
            self.lazy[node] = 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        sum_left = self.query_range(l, r, left, start, mid)
        sum_right = self.query_range(l, r, right, mid + 1, end)
        return sum_left + sum_right
```
```