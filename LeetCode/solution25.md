> 2024.12.29
> 

### [Reverse Nodes in k-Group - LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

---

# Approach

1. Handle edge case(k is 1) → There’s no modification. So It returns head.
2. Count the size of input ListNode → Tracking the LinkedList and record the size of the list.
3. Initiate front, rear
    1. `front`: Top node of k bundle.
    2. `rear` : Last node of k bundle.
4. Iterate input ListNode. 
    1. Using `cnt`  can help separation of bundles.
    2. The `cnt` modulo `k` is zero, then move to next k bundle.
    3. k bundle would be reversed.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/76ae0795-5575-4f38-b716-f3648abce37a/2c943e09-c643-4c6d-86b9-ee45875c3d78/image.png)

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Handle edge case where k is 1 
        # - you don't have to reverse)
        if k == 1:
            return head

        # 2. Count the size of input ListNode
        node, size = head, 0
        while node:
            size += 1
            node = node.next

        # 3. Initiate front, rear 
        top = ListNode(-1)
        top.next = head
        front, rear = top, head

        # 4. Iterate input ListNode. And k bundle would be reversed.
        cnt = 1
        while rear.next:
            if cnt > 1 and cnt%k == 0:
                # not enough to make k bundle.
                if cnt+k > size:
                    break
                
                # move to next k bundle.
                front = rear
                rear = front.next
            else:
                # shift rear's next node to front's next.
                temp = rear.next
                rear.next = rear.next.next
                temp.next = front.next
                front.next = temp
            cnt += 1

        return top.next
```

---

# Complexity Analysis

**Time Complexity**: `O(n)`

1. Conditional instruction.. constant complexity → O(1)
2. Count size: Iterate the ListNode. All of members would be considered. → O(n)
3. Initiate top, front, rear. constant complexity → O(1)
4. Iterate the List Node and reverse them. But the reversal has constant time complexity. → O(n)

**Space Complexity**: `O(1)` → There’s no kind of variable type which has several values.

# Review

Handling LinkedList structure was too difficult. Being used to the structure can help the problem easily.