class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    else:
        l, r = 0, len(nums) -1
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        return root
    
def inorderTraversal(root):
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

test_cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [-10, -3, 0, 5, 9],
    [1, 3, 5, 7, 9, 11, 13, 15]
]

for i, test in enumerate(test_cases):
    print(f"Test case {i+1}: Original array: {test}")
    root = sortedArrayToBST(test)
    result = inorderTraversal(root)
    print(f"          In-order traversal: {result}\n")