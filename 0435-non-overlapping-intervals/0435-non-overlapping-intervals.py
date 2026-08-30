class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l=sorted(intervals,key=lambda x:x[1])
        c=0
        e=l[0][1]
        for i in range(1,len(l)):
            if l[i][0]>=e:
                e=l[i][1]
            else:
                c+=1
        return c