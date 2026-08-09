class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        for i in range(2**len(nums)):
            # 2進数にしてゼロ埋め
            binary_num = format(i, f"0{len(nums)}b")

            res_elm = []
            for j in range(len(binary_num)):
                if binary_num[j] == "1":
                    res_elm.append(nums[j])
            
            res.append(res_elm)
        
        return res
