class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g=[]
        for i in range(m):
            g.append(['#']*n)
        for i in range(m):
            g[i][0]='.'
        for i in range(n):
            g[-1][i]='.'
        res=[]
        for i in g:
            res.append(''.join(i))
        return res