class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevValues = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevValues:
                return [prevValues[difference], i]
            prevValues[n] = i
        return 