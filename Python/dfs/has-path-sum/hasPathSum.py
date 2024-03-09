
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(node, sum):
            if not node:
                return False
            else:
                sum+=node.val
                if not node.left and not node.right:
                    return sum == targetSum
                return helper(node.left, sum) or helper(node.right, sum)
        return helper(root, 0) or False
    
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

sol = Solution()
result = sol.hasPathSum(root, 100)
print(result)