class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        
        while nums1[i] != nums2[j] :
            if nums1[i] > nums2[j] :
                j += 1
            else:
                i += 1
            if i > len(nums1) -1 or j > len(nums2) -1:
                return -1
        
        return nums1[i]
