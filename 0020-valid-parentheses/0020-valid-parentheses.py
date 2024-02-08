class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                # if length of stack = 0 during check means more closed brackets
                if len(stack) == 0:
                    return False
                
                temp = stack.pop()
                
                # if last opening doesnt match the correct then it will return false
                if brackets[temp] != char: 
                    return False

        # if length of stack > 0 after check means more opening brackets
        if len(stack) > 0:
            return False

        return True