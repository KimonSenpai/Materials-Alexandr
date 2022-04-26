# 279 kompege

#abcde

f = open(r"D:\Downloads\24 (4).txt")

s = f.readline()

cnt = 0

if s[:4] == "BOSS" and s[4] != 'J':
    cnt += 1
if s[-4:] == "BOSS" and s[-5] != 'J':
    cnt += 1
for i in range(1, len(s) - 5):
    if s[i-1] == 'J' or s[i + 4] == 'J':
        continue
    if s[i:i+4] == "BOSS":
        cnt += 1

print(cnt)