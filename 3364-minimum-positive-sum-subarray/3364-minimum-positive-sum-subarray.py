class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini=float('inf')
        c=0
        for k in range(l,r+1):
            c=sum(nums[:k])
            if c>0:
                mini=min(mini,c)
            for j in range(k,len(nums)):
                c+=nums[j]-nums[j-k]
                if c>0:
                    mini=min(mini,c)
        if mini==float('inf'):
            return -1
        return mini