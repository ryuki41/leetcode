class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]

        # 斜めの数字の合計を足す
        sum = 0
        for i in range(len(mat)):
            # 左上から右下にかけて
            sum += mat[i][i]
            # 右上から左下にかけて
            sum += mat[i][len(mat)-i-1]
        

        # 行列のサイズが奇数の場合、中心部分の数字が2回カウントされているので、1回分カウントを減らす
        if len(mat) % 2 == 1:
            center_point = len(mat) // 2
            center_num = mat[center_point][center_point]
            sum -= center_num

        return sum