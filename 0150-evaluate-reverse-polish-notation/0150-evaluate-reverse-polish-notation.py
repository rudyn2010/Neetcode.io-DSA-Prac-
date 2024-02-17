class Solution(object):
    def evalRPN(self, tokens):
        
        # Define a dictionary to map operators to their corresponding functions
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        
        # Initialize an empty stack to store operands
        stack = []
        
        # Iterate through each token in the input list
        for i, t in enumerate(tokens):
            if t not in ops:
                # If the token is not an operator, it must be an operand
                # Convert it to an integer and push it onto the stack
                stack.append(int(t))
            else:
                # If the token is an operator, pop the top two operands from the stack
                if stack:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    # Apply the operator function to the operands
                    # Note: For division, we use truediv to handle floating-point results
                    n = int(ops[t](n2,n1))
                    # Push the result back onto the stack
                    stack.append(n)
        
        # The final result is the only value left on the stack
        return stack.pop()