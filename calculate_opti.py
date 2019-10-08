maxN = 64

def value(k):
    return lambda n: n // k + n % k

for k in range(maxN + 1):
    print(k, sum(filter(value(k), range(maxN + 1))) / (maxN + 1))
