class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        self.dfs(root)
        return self.res
    def dfs (self, root):
        if not root: return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
result = sol.inorderTraversal(root)
print(result)