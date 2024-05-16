from typing import Optional

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not (root.left or root.right):
            return root.val
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
