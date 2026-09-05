class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(1<<len(nums)):
            l=[]
            for j in range(len(nums)):
                if i&(1<<j):
                    l.append(nums[j])
            res.append(l)
        return res