> 2024.12.28
> 

### [Merge Two Sorted Lists - LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

---

# Approach

- Create box list.
    - It should be ordered ascending.
    - Iterating 2 lists simultaneously. When both of lists exist, comparing 2 values and smaller one should be inserted to box list. And when only 1 list exists, the list’s members should be inserted to box list in ordered.
- New ListNode to return.
    - Top node → to handle the exception that length of box is zero.
    - return top’s next.

---

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create box list (ordered ascending)
        box = deque([])
        node1, node2 = list1, list2
        while node1 or node2:
            if not node1: # -> append node2's top
                box.append(node2)
                node2 = node2.next
            elif not node2: # -> append node1's top
                box.append(node1)
                node1 = node1.next
            else: # Both of nodes exist.
                # -> Comparing 2 top nodes and smaller one would be appended to box list.
                if node1.val < node2.val:
                    box.append(node1)
                    node1 = node1.next
                else:
                    box.append(node2)
                    node2 = node2.next

        # 2. New ListNode for returning answer.
        top = ListNode(-1) # dummy node
        node = top
        for x in box:
            node.next = x
            node = node.next
        return top.next
```

---

# Complexity Analysis

**Time Complexity**: `O(n)`Let the list1 has n1 members and the list2 has n2 members. All of n1 + n2 members should be considered in iterating. The consideration’s time complexity is constant. Its complexity would be O(n1+n2)…

**Space Complexity**: `O(n)` box list should include n1 + n2 members. So that space complexity is O(n1+n2).

# Review

I used new list box to reduce confusing about ordering.