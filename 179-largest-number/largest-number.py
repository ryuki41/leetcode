class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(str1: str, str2: str):
            # 数字を並べ替えることでどちらの並び順が良いか判定する
            if str2 + str1 < str1 + str2:
                return -1
            else:
                return 1

        str_nums = [str(n) for n in nums]
        largest_num = "".join(sorted(str_nums, key=cmp_to_key(compare)))
        
        if largest_num[0] == "0":
            return "0"
        else:
            return largest_num

        