class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,2]
        for i in range(2,n):
            l.append(l[-1]+l[-2])
        return l[n-1]