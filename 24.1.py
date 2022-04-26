# 105 kompege

# s: FFAAAAILLL
# l: 1212341123

f = open(r"D:\Downloads\24 (3).txt")

s = f.readline()

c = s[0]
l = 1
max_l = 0

for ch in s[1:]:
    if ch == c:
        l += 1
    else:
        max_l = max(max_l, l)
        c = ch
        l = 1
print(max_l)
