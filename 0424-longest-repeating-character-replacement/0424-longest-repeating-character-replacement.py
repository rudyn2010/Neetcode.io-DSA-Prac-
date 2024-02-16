class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Hash map to count the occurances of each character, res is the longest substring we can create with k replacements 
        count = {}
        res = 0
        
        # Left pointer initialized at 0, right pointer will go through every element in the input string, s 
        l = 0
        for r in range(len(s)):
            
            # For the char at position r, we will increment the count of it, 1 + whatever the count currently was (use python method to get current value or 0) 
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Before we update our res, we must check if our current window is valid 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            # Update res to the max that it has ever been, so thats size of window?  
            # Size of window can be gotten by (right - left + 1)
            res = max(res, r - l + 1)
            
        return res