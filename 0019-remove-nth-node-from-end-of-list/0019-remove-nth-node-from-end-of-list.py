# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Create a dummy node, with the next pointer to the head of the list since we are inserting at beginning
        dummy = ListNode(0, head)
        
        left, right = dummy, head
        
        # When n reaches 0 we will have shifted right the number of times we wanted to
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
        
        # We want to delete the node, which here is setting next to the left nodes next pointer
        left.next = left.next.next
        return dummy.next
    
        # Time Complexity: O(n) *two pointer solution