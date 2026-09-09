class Solution:
    def countCommas(self, n: int) -> int:
        c=1000
        res=0
        while c<=n:
            res+=(n-c+1)
            c*=1000
        return res