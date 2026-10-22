class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a=d=1
        for i in range(1,len(nums)):
            a+=nums[i]==(nums[i-1]+1)%len(nums)
            d+=nums[i-1]==(nums[i]+1)%len(nums)
        if a==len(nums):
            return 0 if not nums[0] else min(len(nums)-nums[0],nums[0]+2)
        if d==len(nums):
            return min(len(nums)-nums[-1],nums[-1])+1
        return -1