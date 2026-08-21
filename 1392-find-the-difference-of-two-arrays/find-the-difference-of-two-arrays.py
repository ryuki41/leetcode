class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []
        res1_hash = defaultdict(int)
        res2_hash = defaultdict(int)
        for i in range(len(nums1)):
            if res1_hash[nums1[i]] == 0 and not nums1[i] in nums2:
                res1_hash[nums1[i]] = 1
                res1.append(nums1[i])

        for i in range(len(nums2)):
            if res2_hash[nums2[i]] == 0 and not nums2[i] in nums1: 
                res2_hash[nums2[i]] = 1
                res2.append(nums2[i])
        
        return [res1, res2]