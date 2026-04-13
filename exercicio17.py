import math
a=int(input("digite um número"))
b=int(input("digite outro número"))
c=int(input("digite mais um número"))
delta=b**2-4*a*c
if delta <0:
	print("não há raizes reias")
elif  a ==0:
	print("não é equação do segundo grau")
else:
		x1=(-b+ math.sqrt(delta))/(2*a)
		x2=(-b- math.sqrt(delta))/(2*a)
		print(x1,x2)
		
