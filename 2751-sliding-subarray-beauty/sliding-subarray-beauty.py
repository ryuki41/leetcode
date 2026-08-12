class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = defaultdict(int)

        def get_small_num(x: int) -> int:
            found_cnt = 0
            for num in range(-50, 0):
                found_cnt += counter[num]

                if found_cnt >= x:
                    return num

            return 0
            
        beauty_array = []
        for i in range(k):
            counter[nums[i]] += 1
        
        beauty_array.append(get_small_num(x))

        for i in range(k, len(nums)):
            counter[nums[i-k]] -= 1
            counter[nums[i]] += 1
            beauty_array.append(get_small_num(x))
        
        return beauty_array
        
