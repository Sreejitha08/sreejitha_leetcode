class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res=-1
        for i in range(len(nums)):
            if i!=nums[i]:
                if res==-1:
                    res=nums[i]
                else:
                    res&=nums[i]
        return max(res,0)