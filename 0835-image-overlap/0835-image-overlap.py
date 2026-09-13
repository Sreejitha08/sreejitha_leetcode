class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l1=[]
        l2=[]
        d={}
        res=0
        n=len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    l1.append([i,j])
        for i in range(n):
            for j in range(n):
                if img2[i][j]==1:
                    l2.append([i,j])
        for i in range(len(l1)):
            for j in range(len(l2)):
                r=l2[j][0]-l1[i][0]
                c=l2[j][1]-l1[i][1]
                if (r,c) not in d:
                    d[(r,c)]=0
                d[(r,c)]+=1
                res=max(res,d[(r,c)])
        return res