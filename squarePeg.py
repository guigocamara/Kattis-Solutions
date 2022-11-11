import math

l, r = input().split()

l = int(l)
r = int(r)

if l * math.sqrt(2) <= r * 2:
    print('fits')
else:
    print('nope')

