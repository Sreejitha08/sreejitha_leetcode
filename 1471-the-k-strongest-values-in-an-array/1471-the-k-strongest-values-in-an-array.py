class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res=[]
        l=[]
        arr.sort()
        n=len(arr)-1
        n=n//2
        m=arr[n]
        for i in arr:
            l.append([i,abs(i-m)])
        l1=sorted(l,key=lambda x:(x[1],x[0]),reverse=True)
        for i in range(k):
            res.append(l1[i][0])
        print(m)
        print(l1)
        return res