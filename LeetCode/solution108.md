### [Convert Sorted Array to Binary Search Tree - LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

---

# Approach

To create a height-balanced BST from a sorted array:

1. Use the middle element as the root to ensure balance.
2. Recursively split the left and right subarrays for the left and right subtrees.
3. Use a queue for iterative BFS to build the tree without recursion.

---

# Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        queue = deque([(l, r, root)])

        while queue:
            l, r, node = queue.popleft()
            mid = (l + r) // 2

            if l < mid:
                left_mid = (l + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append((l, mid - 1, node.left))

            if mid < r:
                right_mid = (mid + 1 + r) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append((mid + 1, r, node.right))

        return root

```

---

# Complexity Analysis

**Time Complexity**: `O(n)`

- Each array element is processed once.

**Space Complexity**: `O(n)`

- Space is used for the queue and tree nodes.

---

# Review

This BFS solution avoids recursion and stack overflow, efficiently constructing the tree iteratively. Simpler alternatives like recursion might be easier for smaller inputs.