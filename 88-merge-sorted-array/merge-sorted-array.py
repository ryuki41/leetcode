class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
    
        for i in range(m):
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                nums2.sort()
        
        n_pointer = 0
        for j in range(m, n+m):
            nums1[j] = nums2[n_pointer]
            n_pointer += 1
