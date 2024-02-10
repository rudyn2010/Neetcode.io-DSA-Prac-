class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort input array to find triplets that are zero summed. 
        res = []
        nums.sort()
        
        # We want to use each value from input array as a possible first value when checking triplets. Enumerate function adds a counter to an iterable (in this case an input array).
        for i, a in enumerate(nums):
            
            # Check whether or not the same value is used in same position twice
            if i > 0 and a == nums[i - 1]:
                continue
                
            # Use 2 Pointer method to solve rest of the problem 
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                # Solving: initial value + (L + R) = 0
                threeSum = a + nums[l] + nums[r]
                
                # If sum > 0, we want to decrease our sum. Since input is sorted, shifting to the left has smaller values. 
                if threeSum > 0:
                    r -= 1
                
                # If sum < 0, we want to increase our sum to get 0. Shifting to right has bigger values. 
                elif threeSum < 0:
                    l += 1
                    
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    
                    # Check to see if subsequent values are the same as appended res 
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                        
        return res