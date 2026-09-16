class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ar: int) -> int:
        l=[]
        for i in range(len(capacity)):
            l.append([capacity[i],rocks[i]])
        l1=sorted(l,key=lambda x:x[0]-x[1])
        c=0
        for i in range(len(l1)):
            if l1[i][0]-l1[i][1]<=ar:
                c+=1
                ar-=(l1[i][0]-l1[i][1])
            if ar==0:
                return c
        return c