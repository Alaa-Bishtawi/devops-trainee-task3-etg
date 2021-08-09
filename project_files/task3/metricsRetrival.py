import mysql.connector 

def dbSetup():
    
        mydb = mysql.connector.connect(
                host="db",
                user="root",
                password="123",
                database="test1"
            )
        
    
            
        return mydb

def dbRetrive(usage_type,mydb,NO_OF_RETRIVED_DATA):
    query='SELECT time,{} FROM dataa ORDER BY time DESC;'
    currentCursor=mydb.cursor()
    currentCursor.execute(query.format(usage_type))
    if NO_OF_RETRIVED_DATA==0:
        return currentCursor.fetchmany(NO_OF_RETRIVED_DATA)
    else:   
        return currentCursor.fetchmany(NO_OF_RETRIVED_DATA)

def formatStrDay(usageTypeString,usageList):
    usageStr="Time : {},\t {} usage : {} \n"
    usageListStr=''    
    for usage in usageList:
        usageListStr=usageListStr + usageStr.format(usage[0],usageTypeString,usage[1])
    return usageListStr
def formatStrCurrent(usageTypeString,usageList):
    usageCurrentStr=''
    for usage in usageList:
        usageStr="Time : {},\t {} usage : {} \n"
        usageCurrentStr= usageStr.format(usage[0],usageTypeString,usage[1])
    return usageCurrentStr

def retrive(usageType,usageTypeString,mode):
    mydb=dbSetup()
    usageList=''
    formatedUsage= ''
    if mode == 'day':
        usageList=dbRetrive(usageType,mydb,24)
        formatedUsage=formatStrDay(usageTypeString,usageList)
    elif mode == 'current' :
         usageList=dbRetrive(usageType,mydb,1)
         formatedUsage=formatStrCurrent(usageTypeString,usageList)
    mydb.close()
    return formatedUsage

def cpuDayRetrive():
    CPU_STRING='CPU'
    USAGE_TYPE='cpu'
    MODE='day'
    return retrive(USAGE_TYPE,CPU_STRING,MODE)

def ramDayRetrive():
    RAM_STRING='RAM'
    USAGE_TYPE='ram'
    MODE='day'
    return retrive(USAGE_TYPE,RAM_STRING,MODE)

def hddDayRetrive():
    HDD_STRING='HDD'
    USAGE_TYPE='disk'
    MODE='day'
    return retrive(USAGE_TYPE,HDD_STRING,MODE)

def cpuCurrentRetrive():
    CPU_STRING='CPU'
    USAGE_TYPE='cpu'
    MODE='current'
    return retrive(USAGE_TYPE,CPU_STRING,MODE)

def ramCurrentRetrive():
    RAM_STRING='RAM'
    USAGE_TYPE='ram'
    MODE='current'
    return retrive(USAGE_TYPE,RAM_STRING,MODE)

def hddCurrentRetrive():
    HDD_STRING='HDD'
    USAGE_TYPE='disk'
    MODE='current'
    return retrive(USAGE_TYPE,HDD_STRING,MODE)

