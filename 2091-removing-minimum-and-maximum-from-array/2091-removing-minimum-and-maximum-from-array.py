class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=float('inf')
        minind=-1
        maxi=float('-inf')
        maxind=-1
        for i in range(n):
            if nums[i]<mini:
                mini=nums[i]
                minind=i
            if nums[i]>maxi:
                maxi=nums[i]
                maxind=i
        c1=max(minind,maxind)+1
        c2=n-min(minind,maxind)
        c3=min(minind+1,n-minind)+min(maxind+1,n-maxind)
        return min(c1,c2,c3)
