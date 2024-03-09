class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        def helper(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            helper(root.left, arr)
            helper(root.right, arr)
        arr1, arr2 = [], []
        helper(root1, arr1)
        helper(root2, arr2)
        return arr1 == arr2
    
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right = TreeNode(1)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

sol = Solution()
result = sol.leafSimilar(root1, root2)
print(result)