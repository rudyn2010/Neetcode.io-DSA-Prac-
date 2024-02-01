class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates = set()
        
        for x in nums:
            if x in duplicates:
                return True
            duplicates.add(x)
        return False