t = input("请输入温度，以'C'或者'F'开头。")

if t[0] in ['F']:
    C = (eval(t[1:])-32)/1.8
    print("C{:.2f}".format(C))
elif t[0] in ['C']:
    F = 1.8*eval(t[1:])+32
    print("F{:.2f}".format(F))
