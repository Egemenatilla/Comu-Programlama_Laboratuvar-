----------------------------------
#Üst alma işlemi (fonksiyon)
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*power(a,b-1)
print(power(2,3)) #istenilen değerler girildiğinde işlemin sonucunu çıktı olarak ekrana yazdırır.
-----------------------------------
#Üst kısmının çift olup olmadığı durumunu kontrol eder.
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2==0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a

print(power(5,3))
