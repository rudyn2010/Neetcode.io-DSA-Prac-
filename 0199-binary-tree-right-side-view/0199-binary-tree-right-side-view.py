# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Another BFS - want to look at each level and return the first node on the right
        
        # Will use a Queue for FIFO (right most will be either 1 single value of the level, or the right most value)
        
        ans = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            size = len(q)
            
            for i in range(size):
                
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightSide:
                ans.append(rightSide.val)
            
        return ans
    
        # Time Complexity: O(n) visit each node once
        # Memory Complexity: O(n)