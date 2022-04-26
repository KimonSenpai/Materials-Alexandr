# 706 kompege

# x - value, a - divider x
# x = a*b

def isPrime(val):
    div = 2
    while div*div <= val:
        if val % div == 0:
            return False
        div += 1
    return True

for val in range(6638225, 6638322 + 1):
    if isPrime(val):
        print(val)
    