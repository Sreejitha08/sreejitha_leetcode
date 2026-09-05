class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # if left==0:
        #     return 0
        # c=0
        # n=left
        # while n>1:
        #     n=n>>1
        #     c+=1
        # if right>=(1<<(c+1)):
        #     return 0
        # c=left
        # for i in range(left,right+1):
        #     c&=i
        # return c
        while left<right:
            right=right&(right-1)
        return right