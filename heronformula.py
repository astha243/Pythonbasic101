import math
(a,b,c) = input().split()
(a, b, c) = int(a), int(b), int(c)
p = (a + b + c) / 2
S = math.sqrt(p * ((p - a) * ( p - b) * (p - c)))
print(S)



