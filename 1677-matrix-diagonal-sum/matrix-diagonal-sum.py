class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat) - i - 1]
        
        # 2重にカウントしている場合1つカウントを引く
        if len(mat) % 2 == 1: 
            center = len(mat) // 2
            sum -= mat[center][center]
        
        return sum