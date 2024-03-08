# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # To invert it is to swap the child nodes with each other in position, and by definition we can do this recursively 
        # Visit every single node in the tree, and every time we visit a node we look at the children and swap the position 
        # Then run recursively invertTree on both left and right, DFS (Depth First) 
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root