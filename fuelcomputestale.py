import redishelper
redisCon=redishelper.getRedisInstance()
# import time
import ast
# import datetime as dt
fuelComputeList=redisCon.lrange('FuelComputeStale:'+'861359039995996',0,50)
fuelComputeList=[ast.literal_eval(item.decode()) for item in fuelComputeList]
flen=len(fuelComputeList)
stopindex=-1
maxdelya=15
windowsize=8
filteredFuelList=[]
templist=[]
if flen>11:
    for idx in  range(0,len(fuelComputeList)-1):
        deltatime=abs(int(fuelComputeList[idx]['fuelReportTime'])-int(fuelComputeList[idx+1]['fuelReportTime']))
        if deltatime>maxdelya:
            stopindex=idx
            if len(templist)<windowsize:
                templist=[]
            else:
                filteredFuelList.append(templist)
                templist=[]
        else:
            stopindex=-1
            templist.append(fuelComputeList[idx]) 
if stopindex==-1:
    if len(templist)<8:
        pass
        # redisCon.ltrim('FuelComputeStale:'+'861359039995996',flen-len(templist),-1)
    else:
        filteredFuelList.append(templist)
# else:
    # redisCon.ltrim('FuelComputeStale:'+'861359039995996',flen,-1)

print(filteredFuelList,len(filteredFuelList),len(filteredFuelList[0]),len(filteredFuelList[1]))

def getThresholdspeed(data):
    speedthreshold=2
    filterdata=filter(lambda item:float(item['speed'])<speedthreshold,data)
    filterdata=list(filterdata)
    return filterdata

for k in filteredFuelList:
    k=getThresholdspeed(k)
    print("k==",k,len(k))