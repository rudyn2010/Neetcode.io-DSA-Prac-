# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Follows the general idea of adding 2 numbers, input lists will represent number in reverse order
        dummy = ListNode()
        curr = dummy
        
        # Carry variable is initiated, the value that will be added to the next digit
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # New digit, simple mathematics 
            val = v1 + v2 + carry
            
            # The carry can be found by using mod division by 10 to get reminded of ones digit
            carry = val // 10 
            val = val % 10
            curr.next = ListNode(val)
            
            # Update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
    
    