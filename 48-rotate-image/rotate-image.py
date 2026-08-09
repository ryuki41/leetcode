class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n-i-1):
                # 左上の値を保存しておく
                tmp_num = matrix[i][j]
                # 左下を左上に
                matrix[i][j] = matrix[n-j-1][i]
                # 右下を左下に
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                # 右上を右下に
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                # 左上を右上に
                matrix[j][n-i-1] = tmp_num
        
        return matrix
        