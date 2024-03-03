class Solution:
    def bt(self, root):
        # Start the DFS traversal from the root
        self.dfs(root)

    def dfs(self, root):
        # Recursive DFS function
        if not root:
            return
        print(root.val)  # Process the node (in this case, just printing its value)
        self.dfs(root.left)  # Visit left subtree
        self.dfs(root.right)  # Visit right subtree