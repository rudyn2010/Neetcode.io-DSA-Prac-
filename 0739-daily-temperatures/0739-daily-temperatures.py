class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Answer array will be initialized with zero to the length of the original input array 
        res = [0] * len(temperatures)
        
        # Pair: [temp, index of temp], this is to hold the temp and the index is used to calculate the difference ( or number of days to find a greater temp) 
        stack = []
        
        # Enumerate, python func will get the value and the index from input array 
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
                
            stack.append([t, i])
        return res
    
        # Time Complexity: O(n) / Space Complexity: O(n)