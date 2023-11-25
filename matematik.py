pi = 3.1415

e = 2.7182

def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    return toplam

def çıkarma(a,b):
    return a-b

def çarpma(*a):
    çarpım = 1
    for i in a:
        çarpım *= i
    return çarpım

def bölme(a,b):
    return a/b

def faktöriyel(a):
    faktöriyel = 1
    while a>=1:
        faktöriyel *= a
        a -= 1
    return faktöriyel

def bölen(a):
    liste = []
    for i in range(1,a+1):
        if a%i == 0:
            liste.append(i)
    return liste

def asal_sayı(sayı):
    if sayı == 1:
        return False
    elif sayı == 2:
        return True
    for i in range(2,sayı):
        if sayı%i == 0:
            return False
    return True

def üs_alma(sayı1,sayı2):
    return sayı1 ** sayı2

def taban(x):
    x = int(x)
    return x

def tavan(a):
    a = int(a)
    return a+1

def mutlak_değer(x):
    x = abs(x)
    return x

def bölüm_kalan(a,b):
    b = abs(b)
    return a%b

def ebob(a,b):
    liste1 = []
    liste2 = []
    liste3 = []
    for i in range(1,a+1):
        if a %i == 0:
            liste1.append(i)
    for i in range(1,b+1):
        if b %i == 0:
            liste2.append(i)
    for i in liste1:
        for x in liste2:
            if i==x:
                liste3.append(i)
    return liste3[-1]

def ekok(a,b):
    ekok = 1
    x = 2
    while True:
        if a%x== 0 and b%x == 0:
            ekok *= x
            a = a//x
            b = b//x

        elif a%x!= 0 and b%x == 0:
            ekok *= x
            b = b//x

        elif a%x== 0 and b%x != 0:
            ekok *= x
            a = a//x

        elif a%x!= 0 and b%x != 0:
            x+=1

        if a==1 and b== 1:
            return ekok

def log(a,b):
    for i in range(0,999):
        if a**i == b:
            return i

def karekök(a):
    return a**0.5



