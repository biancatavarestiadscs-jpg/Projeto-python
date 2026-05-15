import random
print ("\033[36m=\033[m"*20)
print("\033[33mJOGO DA ADIVINHAÇÃO \033[m")
print("\033[36m=\033[m"*20)
computador=random.randint(0,10)
numero=int(input("Adivinhe o número que pensei de 0 à 10 \033[34mVOCÊ TEM UMA CHANCE \033[m:"))
if numero == computador:
	print("\033[32mVOCÊ ACERTOU\033[m")
else:
	print("\033[31mVOCÊ ERROU\033[m")
	print("Pensei no número",computador)
computador2=random.randint(20,30)
numero2=int(input("Agora adivinhe  o número  que pensei de 20 à 30\033[34mVOCÊ TEM UMA CHANCE\033[m:"))
if numero2 ==computador2:
	print("\033[32mVOCÊ ACERTOU\033[m")
else:
	print("\033[31mVOCÊ ERROU\033[m")
	print("Pensei no número",computador2)
computador3=["gato","cachorro"]
animal=(input("Agora adivinhe o animal que pensei \033[34mVOCÊ TEM UMA CHANCE\033[m:"))
if animal in computador3:
	print("\033[32mVOCÊ ACERTOU\033[m")
else:
	print("\033[31mVOCÊ ERROU\033[m")
	print("Pensei no animal",computador3)
	
