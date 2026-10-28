class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n=len(grid)
        res=[]
        for i in range(n-2):
            res.append([0]*(n-2))
        for i in range(n-2):
            for j in range(n-2):
                maxi=float('-inf')
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        maxi=max(maxi,grid[k][l])
                res[i][j]=maxi
        return res