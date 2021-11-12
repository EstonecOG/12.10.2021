def arithmetic(a: float,b:float,c=str):
    """Lihtne kalkulaator
    + - liitamine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
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
    else:
        print("Viga!")
    return("")
def is_year_leap(year:int)->bool:
    """Kirjutame suvalise aasta ja programm määrab ära, kas viisaaasta või mitte, kas True või False.
    :param int year:esimene arv
    :rtype str
    """
    if year%4==0:
        t=True
    else:
        t=False
    return("")
def square(kv:float):
    """Kirjutame ruudu külje ja programm annab meile ruudu pindala, perimeetri ja diagonaali
    :param int kv:esimene arv
    :rtype float
    """
    return(4*kv, kv**2, (2*kv**2)**.5)
    return("")
def season(kuu:int):
    """Kirjutame 1-12 kuust ja programm määrab aastaaja kuu kaupa
    :param int kuu: esimene arv
    :rtype str
    """
    if kuu==12 or 1<=kuu<=2:
       print("Зима")
    elif 2<kuu<6:
        print("Весна")
    elif 5<kuu<9:
        print("Лето")
    elif 8<kuu<12:
        print("Осень")
    else:
        print("Viga!")
    return
def bank(a:float,years:int):
    """Paneme raha saldole ja ootame n arv aastaid
    :param float a:Esimene arv
    :param float years: Teine arv
    :rtype float
    """
    for _ in range(years):
        a=((1.1*1/100)*a)*100
    print("Ваш баланс:",a)
    return("")
def is_prime(a:int):
    """Kirjutame arvu vahemikus 0 kuni 1000 ja tagastame tõene, kui see on lihtne, ja  True muul False.
    :param int a:Esimene arv
    :rtype str
    """
    b=2
    while a%b!=0:
        b+=1
    return b==a
def xor_cipher(string:str, key:str)->str:
    """Tavaline sõna kodeeristakse
    :param str string: Esimene arv
    :param str key: Teine arv
    """
    result=""
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i])
        for j in range(len(key)):
            temp^=ord(key[j])
        result+=chr(temp)
    return result
def xor_uncipher(string:str, key: str)->str:
    """koderiumine text dekodeeritakse
    :param str string: Esimene arv
    :param str key: Teine arv
    """
    result = ""
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result
def date(day:int, month:int, year:int):
    """Kirjutame päeva, kuu, aasta, kui seda kalendris pole, siis programm kirjutab False, 
    kui on, siis programm kirjutab True.
    :param int day: Esimene arv
    :param int month: Teine arv
    :param int year: Kolmas arv
    :rtype str:
    """
    set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
    else:
        return False
