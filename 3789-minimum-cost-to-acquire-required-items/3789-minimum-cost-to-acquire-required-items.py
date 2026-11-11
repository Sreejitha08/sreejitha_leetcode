class Solution:
    def minimumCost(self, cost1: int, cost2: int, costboth: int, need1: int, need2: int) -> int:
        c1=(cost1*need1)+(cost2*need2)
        c2=(costboth*max(need1,need2))
        c3=0
        if need1>need2:
            c3=((costboth*need2)+cost1*(need1-need2))
        else:
            c3=((costboth*need1)+cost2*(need2-need1))
        return min(c1,c2,c3)