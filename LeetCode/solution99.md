> 2025-01-09
> 

### [Recover Binary Search Tree - LeetCode](https://leetcode.com/problems/recover-binary-search-tree/?envType=problem-list-v2&envId=binary-tree)

---

# Approach

To solve the problem, we can leverage the properties of a Binary Search Tree (BST):

- An in-order traversal of a BST produces a sorted list of node values.
- If two nodes have been swapped, the sorted order will be disrupted in one or two places.

The solution can be summarized as follows:

1. Perform an in-order traversal of the tree while tracking the previous node.
2. Identify the two nodes that are incorrectly placed:
    - The first node is found when a previous node's value is greater than the current node's value for the first time.
    - The second node is found either during the same disruption or later when the sorted order breaks again.
3. Swap the values of the two identified nodes to restore the BST.
4. This approach modifies the tree in-place and does not require additional storage for the node values.

---

# Code

```python
import sys
sys.setrecursionlimit(10000)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        # In-order traversal: left -> node -> right
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            # Check for incorrect order
            if self.prev and self.prev.val > node.val:
                self.first = self.first if self.first else self.prev
                self.second = node
            self.prev = node

            dfs(node.right)

        # Perform in-order traversal and identify swapped nodes
        dfs(root)
        
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val

```

---

# Complexity Analysis

**Time Complexity**: `O(n)` → The solution performs a single traversal of the tree, visiting each node exactly once.

**Space Complexity**: `O(h)` → The space complexity is determined by the recursion stack during the depth-first traversal, where `h` is the height of the tree. In the worst case (a completely unbalanced tree), this could be `O(n)`, but for a balanced tree, it would be `O(log n)`.

---

# Review

The provided solution is efficient and leverages the properties of BSTs effectively:

1. It correctly identifies the swapped nodes using in-order traversal.
2. The implementation is clean and adheres to the problem constraints by modifying the tree in-place.

Potential improvements include:

- Adding error handling for edge cases (e.g., very large trees where `sys.setrecursionlimit` might not suffice).
- Implementing the solution iteratively to avoid recursion stack limitations.