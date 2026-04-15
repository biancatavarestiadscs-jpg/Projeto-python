print("="*20)
print("\033[1;34mEMPRÉSTIMO BANCÁRIO!\033[m")
print("="*20)
v=float(input("qual o valor do imóvel ?:"))
s=float(input("qual o seu salário ?:"))
p=float(input("quantas parcelas deseja pagar ?:"))
valor=v/p
if valor <= s*0.30:
 print("\033[32mEmpréstimo aprovado\033[m")
else:
 print("\033[31mEmpréstimo negado\033[m")
print("="*14)
print("\033[1m VOLTE SEMPRE!\033[m")
print("="*14)