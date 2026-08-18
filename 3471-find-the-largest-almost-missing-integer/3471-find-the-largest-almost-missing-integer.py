class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if k==len(nums):
            return max(nums)
        if k==1:
            maxi=-1
            for i in d:
                if d[i]==1 and i>maxi:
                    maxi=i
            return maxi
        if d[nums[0]]>1 and d[nums[-1]]>1:
            return -1
        elif d[nums[0]]>1:
            return nums[-1]
        elif d[nums[-1]]>1:
            return nums[0]
        return max(nums[0],nums[-1])