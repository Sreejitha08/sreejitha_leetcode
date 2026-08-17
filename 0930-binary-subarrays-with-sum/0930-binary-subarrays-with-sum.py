class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count1=0
        count2=0
        l=0
        r=0
        n=len(nums)
        c=0
        for r in range(len(nums)):
            c+=nums[r]
            while c>goal:
                c-=nums[l]
                l+=1
            count1+=(r-l+1)
        l=0
        c=0
        if goal==0:
            return count1
        for r in range(len(nums)):
            c+=nums[r]
            while c>goal-1:
                c-=nums[l]
                l+=1
            count2+=(r-l+1)
        return count1-count2