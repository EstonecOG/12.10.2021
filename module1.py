def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param float c: Aritmeetilene tehing
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b 
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("Viga")
        r=0.0
    return r

def is_year_leap(aasta: int):
    """Liigaasta
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsiooni vastus logilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(a):
    """Ruudu külg
    Annab vastust ruudu pindala,diogonaal,ümbermõõt
    :param int külg: Kui pikk külg
    :rtype bool:Funktsiooni vastus valemi järgi
    """
    p = 4*a
    s = a*a
    d = (a**2) / 2
    k = (p, s, d)
    return k

def season(number):
    """Aastaajad
    Saab vastust kuu aastaaja järgi
    :param int number:Kuu
    :rtype bool:Funktisooni järgi saame vastust milline aastaaja on
    """
    if number == 12 or 1 <= number <= 2:
        print("Talv")
    elif  3 <= number <= 5:
        print("Kevad")
    elif 6 <= number <= 8:
        print("Suvi")
    elif 9 <= number <= 11:
        print("Sügis")
    else:
        print("Kirjuta ainult aastaajad")
    n = int(input("Kirjuta kuu numbritega : "))
    return n

def xor_cipher(string: str, key:str)->str:
    """Tavaline sõna kodeeritakse
    """
    result = ''
    temp = int()
    for i in range(len(key)):
        temp = ord(string[i]) #näitab sümboli
          kood
        for j in range(len(key)):
            temp ^= ord(key[j])
        result += chr(temp)
        return result

def xor_uncipher(string: str, key:str)->str:
    """Kodeeritud text dekodeeritakse
    """
    result = ''
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result

def is_prime(a:int):
    """Kirjutame arvu vahemikus 0 kuni 1000 ja tagastame tõene, kui see on lihtne, ja Väär muul juhul.
    """
    b=2
    while a%b!=0:
        b+=1
    return b==a

def date(day:int, month:int, year:int):
    set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
    else:
        return False

def bank(a:float,years:int):
    """Paneme raha saldole ja ootame n arv aastaid
    """
    for _ in range(years):
        a=((1.1*1/100)*a)*100
    print("Ваш баланс:",a)
    return("")