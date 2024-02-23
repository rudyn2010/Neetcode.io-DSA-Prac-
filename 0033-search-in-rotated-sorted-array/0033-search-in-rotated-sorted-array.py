class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initialize two pointers
        l, r = 0, len(nums) - 1
        
        # Condition to run the Binary Search 
        while l <= r:
            
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # Right sorted portion 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1