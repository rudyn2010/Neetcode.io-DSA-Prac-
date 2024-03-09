# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Do this recursively, however initial func only returns one value a boolean so est an inner func
        
        # Inner func will return a pair of values a boolean and the height of the tree
        def dfs(root):
            # Empty tree
            if not root:
                return [True, 0]
            
            # Call dfs on both halves of the tree
            left, right = dfs(root.left), dfs(root.right)
            
            # From the root node find if it is balanced, by taking abs val of both left and right height
            # * Condition for balanced from the root, but also add 2 more conditions 
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) 
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]