class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi=1
        c1=1
        c2=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c1+=1
            else:
                c1=1
            if nums[i]<nums[i-1]:
                c2+=1
            else:
                c2=1
            maxi=max(maxi,c1,c2)
        return maxi