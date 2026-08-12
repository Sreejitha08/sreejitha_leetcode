class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        i=0
        j=0
        maxl=float('-inf')
        while j<len(nums):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            while d[nums[j]]>k:
                d[nums[i]]-=1
                i+=1
            maxl=max(maxl,j-i+1)
            j+=1
        return maxl