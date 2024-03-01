"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Hashmap where we are going to mapping every single old node to the copy of that node we create 
        oldToCopy = { None: None }
        curr = head 
        
        # 2 Passes: 1 pass where we copy the node 2nd where we set the pointer 
        
        # Keep running until the curr node becomes Null
        while curr:
            # First create copy of the node, passing in value at curr node
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        return oldToCopy[head]
    
        # Time Complexity: O(n) in Linear time
        # Space Complexity or memory: O(n) - storing each node into our hash map