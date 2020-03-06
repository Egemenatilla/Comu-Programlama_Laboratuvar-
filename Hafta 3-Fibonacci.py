
#Fibonacci recursive
# 1,1,2,3,5,8,13,21,34.....
def fibo(n):
    #Bu fonksiyon çok fazla tekrar yaptırıyor bu yüzden fazla tercih edilmez
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
def fibo1(n):
    # Bilenen değerleri kümeye atıyoruz böylelikle sürekli n-1 ve n-2 yi hesaplamak
    # zorunda kalmıyoruz daha az işlem yapıyoruz
    known = {0:0,1:1}
    if n in known:
        return known[n]
    else:
        result = fibo1(n-1)+fibo1(n-2)
        known[n] = result
        return result
print(fibo1(6))
