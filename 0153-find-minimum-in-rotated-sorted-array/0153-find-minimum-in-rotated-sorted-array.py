class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Initialize 2 pointers, left will be first at index 0, right is last at len(array) - 1
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        # Keep running the search while conditions are still valid, left is less than right
        while l <= r:
            
            # Here we handle an edge case where a subarray is already sorted initially (value of left is less than value of right) 
            if nums[l] < nums[r]:
                
                # We can update our res with the min of itself and the left most, and break out of loop
                res = min(res, nums[l])
                break
            
            
            # If not sorted, we can conduct our Binary Search and find our midpt and search left or right
            m = (l + r) // 2
            res = min(res, nums[m])
            
            # Right biased, if nums[m] is greater than # indexed at nums[l], search right sorted half 
            if nums[m] >= nums [l]:
                l = m + 1
            
            # Left biased
            else:
                r = m - 1
        
        return res