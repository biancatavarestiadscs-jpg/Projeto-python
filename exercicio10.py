import math 
valorprestacao=float(input("qual o valor da sua prestação ?:"))
multa=float(input("qual a porcentagem da multa de atraso ?:"))
dias=int(input("quantos dias de atraso ?:"))
print("o valor total a pagar é de :",valorprestacao+(valorprestacao*(multa/100)*dias))