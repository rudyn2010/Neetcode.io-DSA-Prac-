class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Estalbish the dimensions of the matrix first
        # ROWS equal length of matrix, guaranteed non empty matrix, COLS equal length of nested list
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Start Binary Search, with established pointers to find the target row
        top, bot = 0, ROWS - 1
        
        while top <= bot:
            # Find middle row and determine whether or not we search L or R
            row = (top + bot) // 2
            # matrix[row][-1] trick to find right most value in matrix
            if target > matrix[row][-1]:
                # Trying to find a bigger value matrix have to right or down so + 1
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
                
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False 