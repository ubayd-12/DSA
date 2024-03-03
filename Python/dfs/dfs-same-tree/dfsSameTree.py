from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Add the import statement for the TreeNode class
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None and q is None:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
    
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

# Link nodes for Tree 1
node1.left = node2
node1.right = node3

# Create nodes for Tree 2
node4 = TreeNode(1)
node5 = TreeNode(2)
node6 = TreeNode(3)

# Link nodes for Tree 2
node4.left = node5
node4.right = node6

# Instantiate Solution and check if trees are the same
solution = Solution()
result = solution.isSameTree(node1, node4)
print(f"Are the two trees the same? {result}")