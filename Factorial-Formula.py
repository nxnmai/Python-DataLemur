def factorial(n):
    if isinstance(n, int):
        ans = 0
        if n > 1: 
            ans += n * factorial(n - 1)
            return ans
        elif n >= 0:
            return 1
    return None