class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=nums[:]
        l.sort()
        s=-1
        e=-1
        for i in range(len(l)):
            if l[i]!=nums[i] and s==-1:
                s=i
            elif l[i]!=nums[i] and s!=-1:
                e=i
        print(s,e)
        if s==-1 and e==-1:
            return 0
        return e-s+1