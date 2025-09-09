class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        sharers = 0
        for i in range(2, n + 1):
            if i - delay > 0:
                sharers += dp[i - delay] % mod
            if i - forget > 0:
                sharers -= dp[i - forget] % mod

            dp[i] = sharers

        ans = 0
        for i in range(n - forget + 1, n + 1):
            ans = (ans + dp[i]) % mod

        return ans

