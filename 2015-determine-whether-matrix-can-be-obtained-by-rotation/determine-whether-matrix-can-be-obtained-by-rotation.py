class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        equal_list = [True] * 4;

        n = len(mat)
        for i in range(n):
            for j in range(n):
                # 回転していない場合
                if mat[i][j] != target[i][j]:
                    equal_list[0] = False
                
                # 90度回転
                if mat[i][j] != target[j][n-i-1]:
                    equal_list[1] = False

                # 180度回転
                if mat[i][j] != target[n-i-1][n-j-1]:
                    equal_list[2] = False

                # 270度回転
                if mat[i][j] != target[n-j-1][i]:
                    equal_list[3] = False

           
        if True in equal_list:
            return True
        return False
        