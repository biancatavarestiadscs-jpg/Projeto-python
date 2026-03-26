import math
h=float(input("qual a altura do tronco da piramide?:"))
Bmenor=float(input("qual o valor da basa menor ?:"))
Bmaior=float(input("qual o valor da base maior ?:"))
print("o volume da piramide é :",h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5))
