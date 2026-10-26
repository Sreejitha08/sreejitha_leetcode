class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        count=0
        c=0
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
                return 0
            c=grid[i][j]
            grid[i][j]=0
            c+=dfs(i+1,j)
            c+=dfs(i-1,j)
            c+=dfs(i,j+1)
            c+=dfs(i,j-1)
            return c
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    res=dfs(i,j)
                    if res%k==0:
                        count+=1
        return count