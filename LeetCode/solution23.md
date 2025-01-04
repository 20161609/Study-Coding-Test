> 2024.12.29
> 

### [Merge k Sorted Lists - LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

---

# Approach

- Initialize a new list(box) → it helps avoid confusiing with the order of the ListNode.
- Iterating ove all the lists. And in each loof, select the smallest one and record the node’s index.

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Create box list
        box = deque([])
        while not all(not x for x in lists):
            # select the smallest top value among lists
            index = -1
            for i in range(len(lists)):
                if lists[i]:
                    if (index==-1) or (lists[index].val > lists[i].val):
                        index = i
            box.append(lists[index])
            lists[index] = lists[index].next
        
        # 2. Return answer
        top = ListNode(-1)
        node = top
        for x in box:
            node.next = x
            node = node.next
        return top.next
```

---

# Complexity Analysis

> Let there be n1 lists and each list has n2 members.
> 

**Time Complexity**: `O(n^2)`  → Entirely there’re n1 loof. And in the loof, considering maximum n2 members and get smallest one. → O(n1 * n2)

**Space Complexity**: `O(n^2)` → box list should have n1*n2 members

---

# Review

- Using box list made it easily to avoid confusing about order to store members.
- Returning answer
    - Top Node → to handle exception(there’s no member)