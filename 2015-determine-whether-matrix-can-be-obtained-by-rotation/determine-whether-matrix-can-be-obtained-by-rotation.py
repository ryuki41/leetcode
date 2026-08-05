class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        all_rotation = [True] * 4

        n = len(mat)
        for i in range(n):
            for j in range(n):
                # 回転しない場合
                if mat[i][j] != target[i][j]:
                    all_rotation[0] = False
                # 90度回転する場合
                if mat[i][j] != target[j][n-i-1]:
                    all_rotation[1] = False
                # 180度回転する場合
                if mat[i][j] != target[n-1-i][n-1-j]:
                    all_rotation[2] = False
                # 270度回転する場合   
                if mat[i][j] != target[n-j-1][i]:
                    all_rotation[3] = False
        
        return any(all_rotation)