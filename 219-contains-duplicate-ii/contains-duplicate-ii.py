class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index_map = {}

        for index, value in enumerate(nums):
            # 値が既に出てきたかをnum_index_mapを見ることで確認
            if value in num_index_map and abs(num_index_map[value] - index) <= k :
                return True

            num_index_map[value] = index

        return False

        