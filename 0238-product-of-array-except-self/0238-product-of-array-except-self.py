class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Create a result output array, giving each initial position a value of one with the length being the same as the input array
        answer = [1] * (len(nums))
        
        # First we are gonna go through the prefixes
        prefix = 1
        for i in range(len(nums)):
            # Put the prefix into our res array, then multiply it 
            answer[i] = prefix
            prefix *= nums[i]
        
        # Start from the end of the input array and go up until the beginning
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            
            # Here we dont store the postfix, we multiply it so we are in theory (postfix * prefix)
            answer[i] *= postfix
            # We have to update our postfix so we multiply it by whatever value happens to be at the index of the input array nums
            postfix *= nums[i]
        
        return answer