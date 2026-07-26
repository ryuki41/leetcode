class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def num_mapping(num: int):
            if num == 0:
                return mapping[num]
            

            digit = 1
            mapped_num = 0
            while num > 0:
                # 1桁ずつ数字を見て、マッピング後の値に変換する
                digit_num = num % 10
                mapped_num += mapping[digit_num] * digit

                num = num // 10
                digit *= 10

            return mapped_num


        nums.sort(key=num_mapping)

        return nums