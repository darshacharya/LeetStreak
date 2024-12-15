"""50. Pow(x, n)"""
def power(x,n):
    def cal_power(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = cal_power(x, n // 2)
        res *= res

        if n % 2 == 1:
            return res * x
        return res

    ans = cal_power(x, abs(n))
    if n <= 0:
        return 1 / ans
    return ans

x = 2
n = 3
print(power(x,n))