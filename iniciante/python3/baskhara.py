import math

A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B**2) - (4*A*C)
R1 = (-B + (math.sqrt(delta)))/(2*A)
R2 = (-B - (math.sqrt(delta)))/(2*A)

print("R1 = {:.5f}\nR2 = {:.5f}".format(R1, R2))