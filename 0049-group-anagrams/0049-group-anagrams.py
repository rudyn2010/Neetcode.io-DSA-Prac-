class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Mapping the character count of each string to the list of Anagrams
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                
            # Python thing lists cant be keys, so we turn them into tuples which is immutable
            res[tuple(count)].append(s)
            
        return res.values()