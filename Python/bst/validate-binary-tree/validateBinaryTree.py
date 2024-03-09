class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
        def helper(lower, node, right):
            if not node: return True
            if lower >= node.val or right <= node.val:
                return False
            return helper(lower, node.left, node.val) and helper(node.val, node.right, right)
        return helper(float('-inf'), root, float('inf'))

node1 = TreeNode(1)
node3 = TreeNode(3)
root1 = TreeNode(2, node1, node3)

node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node4 = TreeNode(4, node3, node6)
root2 = TreeNode(5, node1, node4)

print(isValidBST(root1))
print(isValidBST(root2)) 