class Solution:
    def maximumUnits(self, bT: List[List[int]], ts: int) -> int:
        l=sorted(bT,key=lambda x:x[1],reverse=True)
        c=0
        i=0
        while ts>0 and i<len(l):
            if l[i][0]<=ts:
                c+=(l[i][0]*l[i][1])
                ts-=l[i][0]
            else:
                c+=(ts*l[i][1])
                ts=0
            i+=1
        return c