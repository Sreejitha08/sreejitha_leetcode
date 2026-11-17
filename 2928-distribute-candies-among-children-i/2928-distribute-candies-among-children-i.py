class Solution:
    def distributeCandies(self, n: int, l: int) -> int:
        c=0
        for i in range(l+1):
            for j in range(l+1):
                k=n-i-j
                if 0<=k<=l:
                    c+=1
        return c