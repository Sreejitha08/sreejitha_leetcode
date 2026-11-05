class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            c1=0
            for j in arr2:
                if abs(i-j)>d:
                    c1+=1
            if c1==len(arr2):c+=1
        return c