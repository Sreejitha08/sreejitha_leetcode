class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        nz=0
        c=0
        for i in nums:
            if i>0:nz=1
            c^=i
        if c!=0:
            return len(nums)
        if c==0 and nz==1:
            return len(nums)-1
        return 0