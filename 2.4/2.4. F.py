from math import gcd
from functools import reduce

print(reduce(gcd, [int(input()) for _ in range(int(input()))]))