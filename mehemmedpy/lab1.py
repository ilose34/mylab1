#12
import math

eps=0.001
x=float(input("x'i daxil edin:"))
y=1
z=0
i=1

while abs(y)>eps:
    y=math.sin(x*i)/math.factorial(i)
    i+=2
    z+=y
    
print(z)