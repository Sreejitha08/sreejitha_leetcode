class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        l=0
        maxi=float('-inf')
        c=0
        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                c-=nums[l]
                l+=1
            s.add(nums[r])
            c+=nums[r]
            maxi=max(maxi,c)
        return maxi