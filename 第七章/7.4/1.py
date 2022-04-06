str = input()
b = eval(str[1:])

if str[0] in ['F']:
    c = ( b - 32 ) / 1.8
    print("C{:.2f}".format(c))
else:
    c = b * 1.8 + 32
    print("F{:.2f}".fprmat(c))