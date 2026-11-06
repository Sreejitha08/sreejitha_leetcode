class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a:a[1])
        q=sorted((t,i) for i,t in enumerate(queries))
        d={}
        for i in logs:
            d[i[0]]=0
        res=[0]*len(queries)
        l=0
        r=0
        c=0
        for t,i in q:
            s=t-x
            while r<len(logs) and logs[r][1]<=t:
                n1=logs[r][0]
                d[n1]+=1
                if d[n1]==1:
                    c+=1
                r+=1
            while l<r and logs[l][1]<s:
                n1=logs[l][0]
                d[n1]-=1
                if d[n1]==0:
                    c-=1
                l+=1
            res[i]=n-c
        return res