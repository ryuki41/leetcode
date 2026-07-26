class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 回転させずとも一致するか
        target_match = True
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if target[i][j] != mat[i][j]:
                    target_match = False
                    break
            if not target_match:
                break
        
        if target_match:
            return True

        # 時計回りに90度回転
        target_match = True
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if target[i][j] != mat[j][n-i-1]:
                    target_match = False
                    break
            if not target_match:
                break
        
        if target_match:
            return True
        
        # 180度回転
        target_match = True
        for i in range(n):
            for j in range(n):
                if target[i][j] != mat[n-i-1][n-j-1]:
                    target_match = False
                    break
            if not target_match:
                break
        
        if target_match:
            return True

        # 270度回転    
        target_match = True
        for i in range(n):
            for j in range(n):
                if target[i][j] != mat[n-j-1][i]:
                    target_match = False
                    break
            if not target_match:
                break
        
        return target_match
        
