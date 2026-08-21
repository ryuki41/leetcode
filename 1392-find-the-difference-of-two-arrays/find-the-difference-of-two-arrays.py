class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        res1 = []
        res2 = []

        for i in s1:
            if not i in s2:
                res1.append(i)

        for j in s2:
            if not j in s1:
                res2.append(j)

        return [res1, res2]