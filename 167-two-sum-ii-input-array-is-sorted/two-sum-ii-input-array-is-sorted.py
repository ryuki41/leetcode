class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 数値をキーにindexを値としてもつハッシュを作成
        num_index = {}
        result = []
        for index, num in enumerate(numbers):
            if target - num in num_index:
                result.append(num_index[target-num]+1)
                result.append(index+1)
            num_index[num] = index
        
        return result
