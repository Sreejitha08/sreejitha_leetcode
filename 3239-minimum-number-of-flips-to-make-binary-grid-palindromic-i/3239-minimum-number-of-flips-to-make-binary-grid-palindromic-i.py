class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        cr=0
        cc=0
        for i in grid:
            j1=0
            j2=len(grid[0])-1
            while j1<=j2:
                if i[j1]!=i[j2]:
                    cr+=1
                j1+=1
                j2-=1
        for i in range(len(grid[0])):
            j1=0
            j2=len(grid)-1
            while j1<=j2:
                if grid[j1][i]!=grid[j2][i]:
                    cc+=1
                j1+=1
                j2-=1
        return min(cr,cc)