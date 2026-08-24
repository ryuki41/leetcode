class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums2) == 0:
            return

        m_pointer = m - 1
        n_pointer = n - 1
        for i in reversed(range(len(nums1))):
            if n_pointer == -1:
                nums1[i] = nums1[m_pointer]
                m_pointer -= 1
                continue
            if m_pointer == -1:
                nums1[i] = nums2[n_pointer]
                n_pointer -= 1
                continue

            if nums1[m_pointer] > nums2[n_pointer]:
                nums1[i] = nums1[m_pointer]
                m_pointer -= 1
            else:
                nums1[i] = nums2[n_pointer]
                n_pointer -= 1
            
        

        