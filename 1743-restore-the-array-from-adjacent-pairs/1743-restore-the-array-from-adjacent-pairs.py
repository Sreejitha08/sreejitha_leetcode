class Solution:
    def restoreArray(self, ap: list[list[int]]) -> list[int]:
        g={}
        for i,j in ap:
            if i not in g:
                g[i]=[]
            if j not in g:
                g[j]=[]
            g[i].append(j)
            g[j].append(i)
        s=None
        for i in g:
            if len(g[i])==1:
                s=i
                break
        res=[]
        p=None
        c=s
        while c!=None:
            res.append(c)
            nn=None
            for i in g[c]:
                if i!=p:
                    nn=i
                    break
            p=c
            c=nn
        return res