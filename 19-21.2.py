# problem 1158 kompege

def move(a, b):
    mas = []
    if a == 0 or b == 0:
        return mas
    if a >= 3 and b >= 3:
        mas += [solve(a - 3, b - 3)]
   
    if a % 2 == 0:
        mas += [solve(a//2, a//2)]
    if b % 2 == 0:
        mas += [solve(b//2, b//2)]
    return mas

from functools import lru_cache
@lru_cache(None)
def solve(a, b):
    mas = move(a, b)

    if len(mas) == 0:
        return -0

    if all(v > 0 for v in mas):
        return -max(mas)
    else:
        return -max(v for v in mas if v <= 0) + 1

print('problem 19')
for s in range(1, 90):
    if +1 in move(32, s):
        print(s)

print('problem 20')
for s in range(1, 90):
    if +2 == solve(32, s):
        print(s)

print('problem 21')
for s in range(1, 90):
    if -2 == solve(20, s):
        print(s)
