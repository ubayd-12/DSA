class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
import statistics
class Solution:
    def averageOfLevels(self, root):
        res = defaultdict(list)
        def dfs(root, level):
            nonlocal res
            if not root:
                return
            if root:
                res[level].append(root.val)
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        dfs(root, 0)
        return [statistics.mean(level_values) for level_values in res.values()]
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.averageOfLevels(root))