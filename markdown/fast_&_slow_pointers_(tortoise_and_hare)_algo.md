# Fast & Slow Pointers (Tortoise and Hare) Algorithm

```python
```python
# Fast & Slow Pointers (Tortoise and Hare) Algorithm

## 1. Category / Type
"""
The Fast & Slow Pointers algorithm, also known as the Tortoise and Hare algorithm, falls under the category of pointer algorithms and is often used for problems related to linked lists or cyclic detection.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Fast & Slow Pointers algorithm is to use two pointers moving at different speeds to detect cycles in data structures, primarily linked lists. The "slow" pointer moves one step at a time, whereas the "fast" pointer moves two steps. If a cycle exists, the fast pointer will eventually meet the slow pointer. This meeting point indicates a cycle in the data structure.
"""

## 3. Steps / Flow
"""
1. Initialize two pointers, slow and fast, both pointing to the head of the linked list.
2. Move the slow pointer one step forward and the fast pointer two steps forward in each iteration.
3. Continue this process until either:
   - The fast pointer or its next pointer becomes null, indicating there is no cycle.
   - The fast pointer meets the slow pointer, indicating a cycle exists.
4. If a cycle is detected, optionally find the starting point of the cycle by:
   a. Resetting one pointer to the head of the linked list while keeping the other at the meeting point.
   b. Move both pointers one step at a time until they meet again. The meeting point will be the start of the cycle.
"""

## 4. Time & Space Complexity
"""
| Best  | Average | Worst | Space |
|-------|---------|-------|-------|
| O(n)  | O(n)    | O(n)  | O(1)  |
"""

## 5. Use Cases
"""
- Detecting cycles in a linked list.
- Finding the start of a cycle in a linked list.
- Useful in problems where you need to determine if a repeated sequence exists in a data structure.
"""

## 6. Common Variants
"""
- Cycle detection in arrays.
- Determining the length of a cycle.
- Finding the intersection point of two linked lists.
"""

## 7. Trade-offs
"""
- The algorithm is efficient in terms of space, using only O(1) additional space.
- The simplicity of the algorithm makes it easy to implement and understand.
- However, it only works in structures where two pointers can traverse at different speeds, limiting its application to specific types of problems like linked lists.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that the fast pointer checks both the current and the next node to prevent null pointer exceptions.
- Be cautious when resetting pointers to find the cycle's start; it's easy to make off-by-one errors.
- Remember that this algorithm only detects cycles; it does not provide information about the length of the cycle unless additional steps are taken.
"""

## 9. Classic Problems
"""
- Floyd's Cycle Detection Algorithm: Also known as Floyd’s Tortoise and Hare.
- Linked List Cycle Detection: A standard problem in coding interviews where this algorithm is frequently applied.
"""

## 10. Code Implementation (Demo)
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle detected
```
```