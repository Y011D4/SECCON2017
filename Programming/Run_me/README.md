# Run me!
__Genre__: Programming
__Point__: 100pts

> Run me!
> ```py
> import sys
> sys.setrecursionlimit(99999)
> def f(n):
>     return n if n < 2 else f(n-2) + f(n-1)
> print "SECCON{" + str(f(11011))[:32] + "}"
> ```

## Writeup
This problem is about Fibonacci numbers.
When large Fibonacci numbers are calculated recursively we must memorize the value which has been already calculated.
Therefore the code above should be modified like this:
```py
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
```

```
SECCON{65076140832331717667772761541872}
```
