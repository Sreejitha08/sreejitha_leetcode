class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxi=float('-inf')
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            while i<len(nums1) and j<len(nums2) and  nums1[i]>nums2[j]:
                i+=1
            while i<len(nums1)and j<len(nums2) and nums1[i]<=nums2[j]:
                j+=1
            maxi=max(maxi,j-i-1)
        if i<len(nums1) and j<len(nums2) and nums1[i]<=nums2[j]:
            maxi=max(maxi,j-i-1)
        if maxi<=0:
            return 0
        return maxi