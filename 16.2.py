
# from math import sin

def F(n):
    res = n*n
    if n > 1:
        res += 2*n + 1
        res += F(n - 2) + F(n//3)

    return res


k = F(20) + F(30)

print(F(100))