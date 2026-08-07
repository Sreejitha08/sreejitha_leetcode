class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        p=0
        d=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    for x,y in d:
                        n1=i+x
                        n2=j+y
                        if (n1<0 or n1>=r or n2<0 or n2>=c or grid[n1][n2]==0):
                            p+=1
        return p