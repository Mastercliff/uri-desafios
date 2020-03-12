IN = int(input())

rest = IN % 365
IN = IN - rest
A = int(IN/365)

rest2 = rest % 30
IN = rest - rest2
M = int(IN / 30)

D = int(rest2)

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(A,M,D))