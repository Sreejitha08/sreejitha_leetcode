class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)-1):
            c=nums[i]+nums[i+1]
            if c in s:
                return True
            s.add(c)
        return False