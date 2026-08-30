class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        d={}
        for i in range(len(costs)):
            d[i]=costs[i][0]-costs[i][1]
        d1=sorted(d.items(),key=lambda x:x[1])
        c=0
        for i in range(len(d1)//2):
            c+=costs[d1[i][0]][0]
        for i in range(len(d1)//2,len(d1)):
            c+=costs[d1[i][0]][1]
        return c