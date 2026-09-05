class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # def build(l,r,i,arr,st):
        #     if(l==r):
        #         st[i]=arr[i]
        #         return
        #     m=l+((r-l)//2)
        #     build(l,m,(2*i)+1,arr,st)
        #     build(m,r,(2*i)+2,arr,st)
        #     st[i]=st[(2*i)+1]^st[(2*i)+2]
        
        # st=[0]*len(arr)
        p=[0]*len(arr)
        s=[0]*len(arr)
        total=0
        for i in range(len(arr)):
            total^=arr[i]
            p[i]=total
        c=0
        for i in range(len(arr)-1,-1,-1):
            c^=arr[i]
            s[i]=c
        res=[]
        for i in queries:
            if i[0]==0:
                res.append(p[i[1]])
            elif i[1]==len(arr)-1:
                res.append(total^p[i[0]-1])
            else:
                res.append(total^p[i[0]-1]^s[i[1]+1])
        return res