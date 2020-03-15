from sympy import Symbol
theta=Symbol('theta')

import math
math.sin(theta)

import sympy
sympy.sin(theta)+sympy.sin(theta)
print(2*sin(theta))

print("----------------------------")

u=Symbol('u')
t=Symbol('t')
g=Symbol('g')

theta=Symbol('theta')

from sympy import solve,sin

solve(u*sin(theta)-g*t,t)
print("------------------------------")

x=Symbol('x')
from sympy import Limit,S
l=Limit(1/x,x,S,dir='-') #limit,s burada sonsuzluk belirtir.
print(l)
#l.doit()

print("--------------------------------")
t=Symbol('t')
st=5*t**2+2*t+8

t1=Symbol('t1')
delta_t=Symbol('delta_t')

st1=st.subs({t:t1})

st1_delta=(st.subs({t:t1+delta_t}))

f_d=Limit((st1_delta-st1)/delta_t,0)
print(f_d)
#f_d.doit()
