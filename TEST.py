a, b, c = map(int, input().split(','))
while a + b < c or b + c < a or b + c < a:
    print("0.00")
    a, b, c = map(int, input().split(','))

L = (a + b + c) / 2
s = (L * (L - a) * (L - b) * (L - c)) ** 0.5
print("%0.2f" % s)