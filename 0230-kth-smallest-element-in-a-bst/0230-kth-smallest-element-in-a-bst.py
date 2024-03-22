# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # In Order Iterative Solution using a stack to contain the previous nodes that we need to pop back up to 
        # Once we reach a null node we go back to the previous node which is top of the stack 
        stack = []
        curr = root
        n = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            
            curr = curr.right