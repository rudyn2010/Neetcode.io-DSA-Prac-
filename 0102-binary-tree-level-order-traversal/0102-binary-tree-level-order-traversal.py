# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return a list of lists representing the nodes at each level left to right.
        # Breadth first search on the tree for level order traversal, implement with a queue (FIFO), queue manages sublists
        
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLength = len(q)
            level = []
            for i in range(qLength):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
                    
        return res
            
    # Time Complexity: O(n) visiting each node once
    # Memory Complexity: O(n)