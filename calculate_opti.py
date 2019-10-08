maxN = 64

def value(k):
    return lambda n: (n // k) + (n % k)

for k1 in range(1, 16):
    for k2 in range(1, k1):
        print(k1, k2, sum((n // k1) + (n % k1) // k2 + (n % k1) % k2 for n in range(maxN + 1)) / (maxN + 1))
