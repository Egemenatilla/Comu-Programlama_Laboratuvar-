----Sıradan olmayan bir zar ve onunla ilgili bir kaç fonksiyon-----

from sympy import FiniteSet

def probability(space,event):  #Olasılık hesabıı yapan fonksiyon.
    return len(event)/len(space)

def check_prime(number): #Sayının asal olup olmadığını kontrol eden fonksiyon.
    if number !=1:
        for factor in range(2,number):
            if number %factor==0:
                return False
    else:
        return False
    return True
space=FiniteSet(*range(1,21))
primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
event=FiniteSet(*primes)
p=probability(space,event)
print(p)
