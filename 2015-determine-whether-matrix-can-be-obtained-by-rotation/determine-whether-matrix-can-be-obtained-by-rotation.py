class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        degree_result = [True] * 4
        for i in range(n):
            for j in range(n):
                # 回転しない場合
                if mat[i][j] != target[i][j]:
                    degree_result[0] = False
                # 90度回転する場合
                if mat[i][j] != target[j][n-i-1]:
                    degree_result[1] = False
                # 180度回転する場合
                if mat[i][j] != target[n-i-1][n-j-1]:
                    degree_result[2] = False
                # 270度回転する場合
                if mat[i][j] != target[n-j-1][i]:
                    degree_result[3] = False

        return any(degree_result)