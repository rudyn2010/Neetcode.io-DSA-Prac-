class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Edge case: If input string 1 is longer than second string. Impossible to find permutation of first string in second.  
        if len(s1) > len(s2):
            return False
        
        # We can use hash maps or arrays since we are getting fixed values lowercase a - z, convert those chars to be integers, and we can use those integers and indexes of our array. 
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            
            # Trick here to use python function ord to get integer value of char and subtract it by ord('a') (or 0) to update count by 1
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        
        # Initialize count of matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
            
        l = 0
        
        # For our right pointer we are going to start from where we left off earlier at len(s1)
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
            
        # Since we didnt check outside of loop if matches == 26 we do it here and it will return true or false, return a boolean statement
        return matches == 26