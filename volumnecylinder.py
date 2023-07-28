import math
d=580
l=1190
h=301.5
area=math.acos(((d/2)-h)/(d/2))*((d/2)**2)-((d/2)-h)*(2*(d/2)*h-h**2)**0.5
volume=area*l
print(volume/((10)**6))

v=(3.14*((d/2)**2)*l)
print("tank vol==",v/(10**6))

