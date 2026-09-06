class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        c1=0
        c2=0
        c3=0
        for i,j,k in triplets:
            if target[0]>=i and target[1]>=j and target[2]>=k:
                if target[0]==i:
                    c1=1
                if target[1]==j:
                    c2=1
                if target[2]==k:
                    c3=1
        return c1+c2+c3==3