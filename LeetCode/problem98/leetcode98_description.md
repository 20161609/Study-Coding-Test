### [Validate Binary Search Tree - LeetCode](https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=binary-tree)

### **First (Incorrect) Solution:**

```python
def dfs(node, box):
    if not node:
        return
    if node.left:
        dfs(node.left, box)
    box.append(node.val)  # Appends value directly to the list
    if node.right:
        dfs(node.right, box)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        box = deque([])
        dfs(root, box)
        for i in range(len(box) - 1):
            if box[i] > box[i+1]:  # Checks only for non-decreasing order
                return False
        return True

```

- **Why it failed for [2,2,2]:**
    - The condition `if box[i] > box[i+1]` only ensures that values are non-decreasing.
    - This allows duplicates (e.g., `[2,2,2]`), which violates the BST property requiring **strict inequality**: values in the left subtree must be strictly less than the root, and values in the right subtree must be strictly greater.

---

### **Second (Correct) Solution:**

```python
def dfs(node, box):
    if node.left:
        if not dfs(node.left, box):  # Recursively validates left subtree
            return False
    if box and box[-1] >= node.val:  # Ensures strict ordering
        return False
    box.append(node.val)  # Adds value after validation
    if node.right:
        if not dfs(node.right, box):  # Recursively validates right subtree
            return False
    return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return dfs(root, deque([]))

```

- **Why it works:**
    - Before appending `node.val` to `box`, it checks if `box[-1]` (last value in `box`) is greater than or equal to `node.val`. This enforces strict inequality.
    - Recursively validates the left and right subtrees by returning `False` immediately if any violation is detected.
    - This ensures that duplicates like `[2,2,2]` are correctly identified as invalid.