# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Recursive Algo Base Case - no nodes to traverse through in either array provided
        if not preorder or not inorder:
            return None
        
        # Create a tree node with the first value of the preorder array
        root = TreeNode(preorder[0])
        
        # Want to find the position of pre order node in inorder array 
        mid = inorder.index(preorder[0])
        
        # Build sub trees recursively using sublists (with mid telling us where we want the node)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root