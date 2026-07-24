class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_consecutive_length = 0
        nums_set = set(nums)

        for num in nums:
            if num not in nums_set:
                continue
            
            nums_set.remove(num)
            current_consecutive_length = 1

            # numより大きい値の連続数を数える
            i = 1
            while num+i in nums_set:
                # nums_setから除外することで同じ数の連続数を数えないようにする
                nums_set.remove(num+i)

                current_consecutive_length += 1               
                i += 1

            
            # numより小さい値の連続数を数える
            j = 1
            while num-j in nums_set:
                nums_set.remove(num-j)

                current_consecutive_length += 1               
                j += 1

            max_consecutive_length = max(max_consecutive_length, current_consecutive_length)

        return max_consecutive_length
