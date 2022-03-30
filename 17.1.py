f = open("D:\\Downloads\\17.txt")

prev = int(f.readline())
cnt = 0
max_sum = -20001
for line in f:
    val = int(line)
    if val*prev % 3 == 0:
        cnt += 1
        max_sum = max(max_sum, val + prev)
    prev = val

print(cnt, max_sum)    