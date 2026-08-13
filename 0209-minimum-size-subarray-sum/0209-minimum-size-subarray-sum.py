class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        mini=float('inf')
        c=0
        for j in range(len(nums)):
            c+=nums[j]
            while c>=target:
                mini=min(mini,j-i+1)
                c-=nums[i]
                i+=1
        if mini==float('inf'):
            return 0
        return mini