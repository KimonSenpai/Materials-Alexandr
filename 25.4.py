# 2407 kompege

cnt = 0
for val in range(970*1_031_849, 2_000_000_001, 1_031_849):
    if val%3 == 0 or val % 5 == 0:
        continue
    vcnt = 0
    div = 2
    while div*div <= val:
        if val%div == 0:
            if div % 2 != 0:
                vcnt += 1
            
            if div*div != val and val//div%2 != 0:
                vcnt += 1
        div += 1

    if vcnt > 100:
        cnt += 1

print(cnt)