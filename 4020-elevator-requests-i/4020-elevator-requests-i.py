class Solution:
    def elevatorRequests(self, n: int, r: list[int]) -> int:
        if not r:
            return 0
        c=r[0]
        for i in range(1,len(r)):
            c+=abs(r[i]-r[i-1])
        return c