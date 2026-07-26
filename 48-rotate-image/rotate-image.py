class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                # 左上の値を一時保存
                tmp = matrix[i][j]
                # 左下から左上へ移動
                matrix[i][j] = matrix[n-j-1][i]
                # 右下から左下へ移動
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                # 右上から右下へ移動
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                # 左上から右上へ移動
                matrix[j][n-i-1] = tmp
        