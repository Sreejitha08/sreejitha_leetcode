class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxl=[0]*len(nums)
        minr=[0]*len(nums)
        maxl[0]=nums[0]
        minr[-1]=nums[-1]
        for i in range(1,len(nums)):
            maxl[i]=max(maxl[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            minr[i]=min(minr[i+1],nums[i])
        for i in range(len(nums)):
            if maxl[i]-minr[i]<=k:
                return i
        return -1