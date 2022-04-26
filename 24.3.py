# 587 kompege

f = open(r"D:\Downloads\24 (5).txt")
cnt = 0
for line in f:
    line.replace('А', 'A')
    line.replace('В', 'B')
    line.replace('С', 'C')
    d = {} # {'A': 0, 'B': 0, 'C': 0}

    for c in line:
        if c not in d:
            d[c] = 0
        d[c] += 1

    if d['B'] >= 1.05*d['A']:
        cnt += 1

print(cnt)