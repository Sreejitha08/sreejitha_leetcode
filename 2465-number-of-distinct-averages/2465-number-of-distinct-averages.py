class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        s=set()
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            s.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(s)