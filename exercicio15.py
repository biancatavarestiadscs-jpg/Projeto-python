turno=input("digite o seu turno de trabalho em letras minusculas,noturno ou diurno?")
horas=float(input("quantas horas você trabalhou?"))
if turno=="noturno":
    print("o valor das horas trabalhadas ,no seu salário é ",horas*45)
else:
    print("o valor das horas trabalhadas ,no seu salário é ",horas*37,50)
