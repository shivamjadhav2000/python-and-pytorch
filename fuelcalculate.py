import math

def verticalCylinder(r,h):
    pi=3.1415926
    fuel=(pi*(r**2)*h)
    return round(fuel/(10**6),3)

def VolumeOfSemiCylinder(d,l,h):
    r=d/2
    #area of segment =area of sector -area of triangle
    #area of sector=(0/360)*(pi*r**2)
    #area of tirangle = 1/2*b*h
    # area of sector=cos-1((r-h)/r)*(r**2)
    # area of triangle is ((r**2-(r-h)**2)**0.5)*(r-h)
    if r>h:
        th=r-h
    else:
        th=h-r
    area_of_sector=math.acos(th/r)*(r**2)
    area_of_triangle=((r**2-th**2)**0.5)*th
    area_of_segment=area_of_sector-area_of_triangle
    if h>r:
        volumne_of_cylinder=3.14*(r**2)
        area_of_segment=volumne_of_cylinder-area_of_segment
    desiel_volume=area_of_segment*l
    return round(desiel_volume/(10**6),3) 

def calculateFuel(TankType,dimensions,fuelLevel):
    if TankType=='cuboid':
        l,b,h=dimensions['l'],dimensions['b'],dimensions['h']
        fuel=l*b*fuelLevel
        return round(fuel/(10**6),3)
    elif TankType=='cylinder':
        d,l=dimensions['d'],dimensions['l']
        return VolumeOfSemiCylinder(d,l,fuelLevel)
    elif TankType=='verticalcylinder':
        r,h=dimensions['r'],dimensions['h']
        return verticalCylinder(r,fuelLevel)

dimensions={
  "l": 1143,
  "d": 558.8
}
fuelheights=[142,125]
print(calculateFuel('cylinder',dimensions,fuelheights[0]))
print(calculateFuel('cylinder',dimensions,fuelheights[1]))
