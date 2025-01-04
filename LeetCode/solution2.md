### [Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/description/)

---

> 2024.12.23
> 

# Approach

- Get 2 values:
    - Iterating 2 ListNodes can offer digits’ numbers.
    - Digits are stored in reverse order. So it should add new digit to left side.
    - If 2 numbers have different digit counts, shorter one would store ‘0’.
    - 2 numbers are stored in String type.
- Get addition
    - Convert type
        1. Deque → String → Int: The list having numbers that’s been stored in string type.
        2. Addition: get sum of 2 numbers
        3. Int → String: to iterate the digits in reverse order.
    - Returning answer
        - top Node: Parent Node of answer Node. (The value -1 has no meaning.)
        - Iterating digits in reverse order and store them to ListNode.

---

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Get 2 values from l1 and l2
        n_list1 = []
        box1, box2 = deque([]), deque([])

        # Track all node in l1, l2 and store values.
        while l1 or l2:
            # If the node exists, the val would be stored.
            # If not, 0 would be stored. (to match the digits)
            if l1:
                box1.appendleft(f'{l1.val}')
                l1 = l1.next
            else:
                box1.appendleft('0')

            if l2:
                box2.appendleft(f'{l2.val}')
                l2 = l2.next
            else:
                box2.appendleft('0')

        # Creating Node for returning answer
        top = ListNode(-1)
        cur_node = top

        # Iterating sum of 2 values and all digits values are stored..
        for x in str(int(''.join(box1)) + int(''.join(box2)))[::-1]:
            cur_node.next = ListNode(int(x))
            cur_node = cur_node.next

        return top.next
```

---

# Complexity Analysis

**Time Complexity**: O(n) → Iterating all nodes in 2 ListNodes.

**Space Complexity**: O(n) → Storing all nodes’ info in 2 ListNodes.

# Review

Since the process of type conversion came up several times, I had to consider a lot about readability.