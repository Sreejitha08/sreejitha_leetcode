class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        d={}
        c=0
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==1:
                return -1
            c+=(d[i]+2)//3
        return c