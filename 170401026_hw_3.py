'''
Egemen ATİLLA 170401026
https://github.com/Egemenatilla/Comu-Programlama_Laboratuvar--/blob/master/170401026_hw_3.py
'''

import sympy as sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt

number = 170401026
l = Symbol('lambda')
x = Symbol('x')



#Poisson Dağılımı:Olasılık kuramı ve istatistik bilim kollarında bir ayrık olasılık dağılımı olup belli bir sabit zaman birim aralığında
#meydana gelme sayısının olasılığını ifade eder.
#Örneğin sabit bir radyasyon altında bir DNA diziliminde meydana gelen mutasyon sayıları (8 saatte 24 mutasyon)
#x = 24 , lambda = 8


my_f_part_0 = l**x #lambda üzeri x
#pprint(my_f_part_0)
my_f_part_1 = sym.exp(-l) # exp e üzeri demek.
#pprint(my_f_part_1)
my_f_part_2 = 1 / sym.factorial(x) #factorial ile faktoriyel işlemini uygulayabildik.
#pprint(my_f_part_2)

poisson_p_d=(my_f_part_0)*(my_f_part_1)*(my_f_part_2)
print("Dağılımın Formülü:")
pprint(poisson_p_d)

a=sym.plot(poisson_p_d.subs({l:8}), (x,0,24), title = 'Poisson Probability Distribution') #sympy ile grafiği bastıran kod parçacığı

x1__values = []
y__values = []

print("Formüle yazdığımız x değeri ve çıkan sonuçlar:\n")
#matplotlib ile grafik.
for value in range(25):                             
    y = poisson_p_d.subs({l:8, x:value}).evalf()
    print(value, y)
for i in range(25):
    y = poisson_p_d.subs({x:i, l:8}).evalf()# Bu kod satırında x1'e karşılık gelen y değerleri bulunur.
    x1__values.append(i)
    y__values.append(y)

a
plt.plot(x1__values, y__values)#Listelediğimiz değerleri grafiğe dönüştürdük
plt.show()#Bu kod satırının yardımıyla grafiği bastırdık.
