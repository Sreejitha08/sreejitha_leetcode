class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        c=0
        t=sum(nums)-x
        i=0
        maxi=float('-inf')
        for j in range(len(nums)):
            c+=nums[j]
            while i<=j and c>t:
                c-=nums[i]
                i+=1
            if c==t:
                maxi=max(maxi,j-i+1)
        if maxi==float('-inf'):
            return -1
        return len(nums)-maxi