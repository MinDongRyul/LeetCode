class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        ret = [(rStart, cStart)] 
        
        # lambda
        is_valid = lambda row, col: row >= 0 and row < rows and col >= 0 and col < cols

        steps = 1 
        r, c = rStart, cStart 
        while len(ret) < rows * cols: 
            # Go east 1
            for step in range(steps):
                r, c = r, c + 1 
                if is_valid(r, c): ret.append((r, c))
                    
            # Go down 1 
            for step in range(steps):
                r, c = r + 1, c 
                if is_valid(r, c): ret.append((r, c))
                    
            steps += 1
                    
            # Go west 2 
            for step in range(steps):
                r, c = r, c - 1
                if is_valid(r, c): ret.append((r, c))           
            
            # Go north 2 
            for step in range(steps):
                r, c = r - 1, c 
                if is_valid(r, c): ret.append((r, c))           
                    
            steps += 1
            
        return ret