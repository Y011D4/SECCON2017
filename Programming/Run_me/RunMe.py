import sys
dp = [-1]*11012
sys.setrecursionlimit(99999)
def f(n):
    if(dp[n]!=-1):
        return dp[n]
    else:
        dp[n] = n if n<2 else f(n-2) + f(n-1)
        return dp[n]
print("SECCON{" + str(f(11011))[:32] + "}")
