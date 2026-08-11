class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        c1=0
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]<=upper:
                c1+=(j-i)
                i+=1
            else:
                j-=1  
        c2=0
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]<=lower-1:
                c2+=(j-i)
                i+=1
            else:
                j-=1    
        return c1-c2