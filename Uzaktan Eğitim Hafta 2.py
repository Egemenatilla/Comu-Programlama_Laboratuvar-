from sympy import Symbol

#çarpanlara ayırma,iki değişkeni matematiksel olarak çarpma
x=Symbol('x')
y=Symbol('y')

p=x*(x+x)
#print(p)

a=(x+2)*(x+3)
#print(a)

#factor ve expand

from sympy import factor,expand
expr=x**2-y**2
#print(factor(expr))
factors=factor(expr)
#print(expand(factors))

expr=x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr)
#print(factors)

from sympy import pprint
#pprint(factors)

#seriler

x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i
#pprint(series)

expr=x*x+x*y+x*y+y*y  
res=expr.subs({x:1,y:2}) #yukarıdaki işlemi değişkenlerin değerlerine göre yapar.
print(res)

r=expr.subs({x:1-y}) #y'yi x cinsinden yazarak işlemi tek değişkene indirger.
print(r)

x=Symbol('x') #Tek değişkene bağlı bir seri yazdık ve değişkene bir değer atadık.
series=x      #İşlemin sonucunu çıktı olarak geri döndürdü
n=5
x_value=10
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)
series_value=series.subs({x:x_value})
print(series_value)

import sympy as sym
from sympy import Symbol
from sympy import pprint

import sympy.plotting as syp
sigma=Symbol('sigma')
x=Symbol('x')
mu=Symbol('mu')


a=2*sym.pi*sigma
#print(a)
#pprint(a) 

b=sym.sqrt(2*sym.pi*sigma)
#pprint(b)

c=sym.sqrt(2*sym.pi*sigma*sigma)
#pprint(c)

part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/2*sigma**2)

my_gauss_function=part_1*part_2
#pprint(my_gauss_function)

#pprint(syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution'))#bir fonksiyon yazdık değişkenlere değerler atadık ve grafiği çizildi.

%matplotlib inline
import matplotlib.pyplot as plt
x_values=[]
y_values=[]
for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).doit() 
    y_values.append(y)
    x_values.append(value)
    print(value,y)
    
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
