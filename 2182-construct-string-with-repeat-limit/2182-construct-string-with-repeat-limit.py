class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d1=sorted(d.items(),key=lambda x:x[0],reverse=True)
        l=[]
        res=""
        for i,j in d1:
            l.append([i,j])
        i=0
        while i<len(l):
            res+=l[i][0]*min(l[i][1],r)
            l[i][1]-=min(l[i][1],r)
            if l[i][1]==0:
                i+=1
                continue
            j=i+1
            while j<len(l) and l[j][1]==0:
                j+=1
            if j==len(l):
                break
            res+=l[j][0]
            l[j][1]-=1
        return res