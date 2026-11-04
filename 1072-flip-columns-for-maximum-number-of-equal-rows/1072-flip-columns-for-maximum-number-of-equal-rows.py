class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        d=Counter()
        for i in matrix:
            p=tuple(x^i[0] for  x in i)
            d[p]+=1
        maxi=float('-inf')
        for i in d:
            maxi=max(maxi,d[i])
        return maxi