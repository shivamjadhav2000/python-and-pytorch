from ast import Delete
import redishelper
import statistics
redisCon=redishelper.getRedisInstance()
FuelLastTime='1662192171'
def getThresholdspeed(data):
    # speed=map(lambda x:float(x[1][b'speed'] for x in data))
    filterdata=filter(lambda item:float(item[1][b'speed'])<2,data)
    filterdata=list(filterdata)
    return filterdata
def get_stable_fuel(data):
    if len(data)>=8:
        fuellist=map(lambda x:float(x[1][b'fuellevel']),data)
        stable_fuel=statistics.median(fuellist)
        print('stable_fuel==',stable_fuel)
def main():
    FuelcurrenTime=str(int(FuelLastTime)+120)
    print(FuelLastTime,'----',FuelcurrenTime)
    l=redisCon.xrange('mystream',FuelLastTime+'-0',FuelcurrenTime+'-0',count=10)
    # print(l,len(l),type(l),"--------------------------------\n\n")
    for i in l:
        print(i[0],i)
    filterdata=getThresholdspeed(l)
    get_stable_fuel(filterdata)
p=redisCon.hgetall('p')
print(p,type(p))
for key,value in p.items():
    print(key,value,type(key),type(value))


# update last fuel stable
# Delete records
# last fetch time stamp

# print(filterdata,len(filterdata))





# print(l)
# d=['1662196598480-0','1662196599459-0']
# redisCon.xdel('kk',*d)