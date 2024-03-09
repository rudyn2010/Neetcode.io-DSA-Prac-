# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Depth First Search, doing pre-order dfs with a stack iteratively 
        if not root:
            return 0
        # [[node, depth]]
        stack = [[root, 1]]
        res = 1
        
        while stack:
            # Pop the node and its depth
            node, depth = stack.pop()
            
            if node:
                # Set the res to the max of its self and the depth we just popped
                res = max(res, depth)
                
                # Add the children of the node and we want to add the depth as well, even if they are null
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth +1])
        
        return res