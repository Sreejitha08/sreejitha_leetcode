class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp=[float('inf')]*(max(max(coins),amount)+1)
        # for i in coins:
        #     dp[i]=1
        # dp[0]=0
        # for i in range(len(dp)):
        #     if dp[i]==float('inf'):
        #         for j in range(i):
        #             if dp[j]!=float('inf') and dp[i-j]!=float('inf'):
        #                 dp[i]=min(dp[i],dp[j]+dp[i-j])
        # if dp[amount]==float('inf'):
        #     return -1
        # return dp[amount]
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if j<=i:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]