from module1 import *
while True:
    print("Funktsioonid" .center(50,"+"))
    print("arithmetic- A,is_year_leap-Y,square-N,O-season")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sissesta aasta")))
        print(rezult)
    elif v.upper()=="N":
        rezult=square(int(input("Sissesta külje pikkus")))
        print(rezult)
    elif v.upper()=="O":
        rezult=season(int(input("Sissesta kuu numbritega")))
        print(rezult)
    elif v.upper()=="X":
        rezult=xor_cipher(input("Sisesta text"), input("Sisesta võti: "))
        print(rezult)
        print("dekodeerimine" .center(60,"*"))
        de_rezult=xor_uncipher(rezult, input"Sisesta võti: "))
        print(de_rezult)
    elif v.upper()=="F":
        a=int(input("Sisestage number: "))
        result=is_prime(a)
        print(result)
    elif v.upper()=="G":
        day=int(input("Sisestage päev: "))
        month=int(input("Sisestage kuu: "))
        year=int(input("Sisestage aasta: "))
        result=date(day,month,year)
        print(result)
    elif v.upper()=="E":
        a=float(input("Sisestage sissemakse summa: "))
        years=int(input("Mitu aastat on möödunud?"))
        result=bank(a,years)
        print(result)
        