class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        nums.sort()
        p=nums[0]%2
        for i in range(1,len(nums)):
            f=False
            if nums[i]%2==p:
                continue
            else:
                for j in range(i):
                    if nums[i]-nums[j]>=1 and (nums[i]-nums[j])%2==p:
                        f=True
                        break
                if f==False:
                    return False
        return True