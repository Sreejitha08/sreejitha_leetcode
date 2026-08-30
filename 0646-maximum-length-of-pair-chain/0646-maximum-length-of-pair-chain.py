class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        l=sorted(pairs,key=lambda x:x[1])
        c=1
        e=l[0][1]
        for i in range(1,len(l)):
            if e<l[i][0]:
                e=l[i][1]
                c+=1
        return c