# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Two Pointer - slow + fast pointers where slow is shifted by one and fast is shifted by 2
        slow, fast = head, head
        
        # There is a cycle if the two pointers will reach each other, if there was no cycle fast pointer would reach end first without ever meeting. 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
    
        # Time Complexity: O(n)
        # Memory Complexity: O(1)