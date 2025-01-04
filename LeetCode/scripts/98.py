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
