# 506 kompege



def isPrime(val):
    div = 2
    while div*div <= val:
        if val % div == 0:
            return False
        div += 1
    return True


for val in range(25317, 51237 + 1):
    div = 2
    divs = []
    while div*div <= val:
        if val % div == 0:
            if isPrime(div):
                divs += [div]
            if div*div != val and isPrime(val//div):
                divs += [val//div]
        div += 1
    
    if len(divs) >= 6:
        print(val, max(divs))