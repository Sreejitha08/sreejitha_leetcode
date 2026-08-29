class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary=""
        for i in s:
            n=bin(ord(i))[2:]
            n='0'*(8-len(n))+n
            binary+=n
        i=0
        j=len(binary)-1
        while i<=j:
            if binary[i]!=binary[j]:
                return False
            i+=1
            j-=1
        return True