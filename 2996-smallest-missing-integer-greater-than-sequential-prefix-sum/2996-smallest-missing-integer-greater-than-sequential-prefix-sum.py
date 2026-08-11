class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        c=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                c+=nums[i]
            else:
                break
        while c in nums:
            c+=1
        return c