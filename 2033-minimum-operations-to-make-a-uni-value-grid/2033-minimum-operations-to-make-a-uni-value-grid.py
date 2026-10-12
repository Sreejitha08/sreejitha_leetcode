
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # /nums = []

        # for row in grid:
        #     nums.extend(row)

        # rem = nums[0] % x

        # for num in nums:
        #     if num % x != rem:
        #         return -1

        # nums.sort()
        # median = nums[len(nums) // 2]

        # ans = 0
        # for num in nums:
        #     ans += abs(num - median) // x

        # return ans
        l=[]
        for i in grid:
            for j in i:
                l.append(j)
        r=l[0]%x
        for i in l:
            if i%x!=r:
                return -1
        l.sort()
        m=l[len(l)//2]
        res=0
        for i in l:
            res+=abs(i-m)//x
        return res