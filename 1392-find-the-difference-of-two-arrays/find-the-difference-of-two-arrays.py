class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer1 = []
        answer2 = []

        nums1 = set(nums1)
        nums2 = set(nums2)

        for num1 in nums1:
            if not num1 in nums2:
                answer1.append(num1)

        for num2 in nums2:
            if not num2 in nums1:
                answer2.append(num2)
        
        return [answer1, answer2]