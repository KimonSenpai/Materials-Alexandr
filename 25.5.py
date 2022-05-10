# 2592 kompege
#2^q * p^4
def isPrime(val):
    div = 2
    while div*div <= val:
        if val % div == 0:
            return False
        div += 1
    return True
l = 55000000000
r = 60000000000
p = 3
res = []
while p**4 <= r:
    q = 0
    while 2**q * p**4 <= r:
        if 2**q * p**4 >= l:
            res += [(2**q * p**4, p**4)]
        q += 1
    p += 1
    while not isPrime(p): p += 1

res.sort()
for p in res:
    print(*p)