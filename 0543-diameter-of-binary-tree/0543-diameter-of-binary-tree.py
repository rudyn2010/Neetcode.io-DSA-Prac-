# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global result variable
        res = [0]
        
        # Est hlper function, that performs the depth first search at the root
        def dfs(root):
            # Edge case if there is no root, an empty trees height is not 0 its -1 cuz height of a single node is 0
            if not root:
                return -1
            
            # Run dfs on both sides
            left = dfs(root.left)
            right = dfs(root.right)
            
            # 2 + left + right will give us diameter
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        
        return res[0]