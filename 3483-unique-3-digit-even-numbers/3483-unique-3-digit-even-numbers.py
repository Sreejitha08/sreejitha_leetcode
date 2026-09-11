class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or i==k or digits[i]==0 or digits[k]%2!=0:
                        continue
                    n=digits[i]*100+digits[j]*10+digits[k]
                    s.add(n)
        return len(s)