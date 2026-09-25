class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        maxi=float('-inf')
        c=0
        res=-1
        for i in range(1950,2051):
            c=0
            for j in range(len(logs)):
                if logs[j][0]<=i and i<logs[j][1]:
                    c+=1
            if c>maxi:
                maxi=c
                res=i
        return res