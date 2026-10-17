class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            n2=nums[i]
            n=nums[i]
            c=0
            while n>0:
                c+=(n%10)
                n//=10
            l.append([n2,c,i])
        res=sorted(l,key=lambda x:[x[1],x[0]])
        v=[False]*len(nums)
        c=0
        for i in range(len(nums)):
            if v[i] or res[i][2]==i:
                continue
            cycle=0
            j=i
            while not v[j]:
                v[j]=True
                j=res[j][2]
                cycle+=1
            c+=(cycle-1)
        return c