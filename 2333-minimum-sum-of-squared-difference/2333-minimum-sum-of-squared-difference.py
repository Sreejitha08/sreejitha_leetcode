class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        l=[]
        for i in range(len(nums1)):
            l.append(abs(nums1[i]-nums2[i]))
        k=k1+k2
        if sum(l)<=k:
            return 0
        low=0
        h=max(l)
        while low<h:
            m=(low+h)//2
            n=sum(max(0,x-m) for x in l)
            if n<=k:
                h=m
            else:
                low=m+1
        level=low
        u=sum(max(0,x-level) for x in l)
        res=sum(min(x,level)**2 for x in l)
        r=k-u
        res-=(r*(2*level-1))
        return res