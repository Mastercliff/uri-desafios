V = input().split()
A = float(V[0])
B = float(V[1])
C = float(V[2])
pi = 3.14159
TRIANGULO = (A*C)/2
CIRCULO  = pi * C**2
TRAPEZIO = (B + A) * C/2
QUADRADO = B**2
RETANGULO = A*B
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}"
.format(TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))