class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pre=[float('inf')]*len(arr)
        suf=[float('inf')]*len(arr)
        mini=float('inf')
        c=0
        i=0
        for j in range(len(arr)):
            c+=arr[j]
            while  c>target:
                c-=arr[i]
                i+=1
            if c==target:
                mini=min(mini,j-i+1)
            pre[j]=mini
        i=len(arr)-1
        c=0
        mini=float('inf')
        for j in range(len(arr)-1,-1,-1):
            c+=arr[j]
            while  c>target:
                c-=arr[i]
                i-=1
            if c==target:
                mini=min(mini,i-j+1)
            suf[j]=mini
        res=float('inf')
        for i in range(len(arr)-1):
            if pre[i]!=float('inf') and suf[i+1]!=float('inf'):
                res=min(res,pre[i]+suf[i+1])
        if res==float('inf'):
            return -1
        print(pre)
        print(suf)
        return res