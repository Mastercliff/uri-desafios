IN = int(input())

rest = IN % 3600
IN = IN - rest
H = int(IN/3600)

rest2 = rest % 60
IN = rest - rest2
M = int(IN / 60)

S = int(rest2)

print("{}:{}:{}".format(H,M,S))