class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        c=0
        nums=[abs(i) for i in nums]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            c+=(nums[j]**2)
            c-=(nums[i]**2)
            j-=1
            i+=1
        if len(nums)%2!=0:
            c+=(nums[j]**2)
        return c