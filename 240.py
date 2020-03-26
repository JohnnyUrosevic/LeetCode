class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        valid_rows = range(len(matrix))
        valid_cols = range(len(matrix[0]))
        
        while valid_rows and valid_cols:
            first_col = valid_cols[0]
            last_col = valid_cols[-1]
            
            new_rows = []
            for i in valid_rows:
                if target == matrix[i][last_col] or target == matrix[i][first_col]:
                    return True
                elif matrix[i][last_col] > target and matrix[i][first_col] < target:
                    new_rows.append(i)

            
            valid_rows = new_rows
            if not valid_rows:
                return False
            
            first_row = valid_rows[0]
            last_row = valid_rows[-1]

            new_cols = []
            for i in valid_cols:
                if target == matrix[first_row][i] or target == matrix[last_row][i]:
                    return True
                elif matrix[first_row][i] < target and matrix[last_row][i] > target:
                    new_cols.append(i)

            valid_cols = new_cols
            
        return False