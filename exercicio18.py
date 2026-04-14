ano=int(input("digite um ano para verificar se é bissexto:"))
if ano % 4==0 and ano % 100 != 0 or ano % 400==0:
    print("="*20)
    print("o ano é bissexto")
    print("="*20)
else:
    print("="*20)
    print("o ano não é bissexto")
    print("="*20)
print("volte sempre")
