# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive Function Depth Fisrt Search
        
        # 1st base case: both trees are empty
        if not p and not q:
            return True
        
        # 2nd base case: 1 of the tree's is null 
        if not p or not q: 
            return False
        
        # 3rd base case: both trees are none empty and the values are not the same
        if p.val != q.val:
            return False
        
        # Call the recursive step here (values are the same)
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))