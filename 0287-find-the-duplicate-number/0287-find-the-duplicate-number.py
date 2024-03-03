class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Start with 2 pointer algo, slow and fast both initiated at 0 since theyll be outside of the cycle
        
        # First part - this is where we figure out where fast and slow intersect
        slow, fast = 0, 0
        
        # Keep going until they intersect 
        while True:
            
            # Set the slow pointer, and fast to one more
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # Initiate a second slow pointer, and continue until first slow and second slow intersect  
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow