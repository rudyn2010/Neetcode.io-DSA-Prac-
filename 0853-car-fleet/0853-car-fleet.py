class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create an array of pairs initially, in python we iterate through the position and speed array simultaniously using zip - list comprehension   
        pair = [[p, s] for p, s in zip(position, speed)]
        
        # Stack will keep track of how many car fleets we have at the end
        stack = []
        
        # Loop through reverse sorted order
        for p, s in sorted(pair)[::-1]: 
            
            # Go through every single car, we want to know what time its going to reach destination using ((target - position) / speed)
            stack.append((target - p) / s)
            
            # Check if there are multiple cars and if speed of position 1 is less than pos 2 (ahead of it or next one)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)