class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def compare(num: int):
            new_st_num = ""
            st_num = str(num)
            
            for st in st_num:
                new_st_num += str(mapping[int(st)])
            
            return int(new_st_num)

        return sorted(nums, key=compare)
            
        