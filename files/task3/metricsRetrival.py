import mysql.connector  #pip install mysql-connector-python
import logging
def dbSetup():
    
        mydb = mysql.connector.connect(
                host="db",
                user="root",
                password="123",
                database="test1"
            )
        
    
            
        return mydb

def dbRetriveDay(usage_type,mydb):
    NO_OF_RETRIVED_DATA=24
    query='SELECT time,{} FROM dataa'
    currentCursor=mydb.cursor()
    currentCursor.execute(query.format(usage_type))
    return currentCursor.fetchmany(NO_OF_RETRIVED_DATA)

def dbRetriveCurrent(usage_type,mydb):
    query='SELECT time,{} FROM dataa'
    currentCursor=mydb.cursor()
    currentCursor.execute(query.format(usage_type))
    return currentCursor.fetchall(),currentCursor.rowcount

def formatStrDay(usageTypeString,usageList):
    usageStr="Time : {},\t {} usage : {} \n"
    usageListStr=''    
    for usage in usageList:
        usageListStr=usageListStr + usageStr.format(usage[0],usageTypeString,usage[1])
    return usageListStr
def formatStrCurrent(usageTypeString,usageList,rc):
    LAST_ROW=-1
    usageStr="Time : {},\t {} usage : {} \n"
    j=0
    usageCurrentStr= ''
    for x in usageList:
        if j<=rc:
            usageCurrentStr= usageStr.format(x[0],usageTypeString,x[1])
        else:
            continue
    
    return usageCurrentStr

def retrive(usageType,usageTypeString,mode):
    mydb=dbSetup()
    usageList=''
    formatedUsage= ''
    if mode == 'day':
        usageList=dbRetriveDay(usageType,mydb)
        formatedUsage=formatStrDay(usageTypeString,usageList)
    elif mode == 'current' :
        
        usageList,rc=dbRetriveCurrent(usageType,mydb)
        
        formatedUsage=formatStrCurrent(usageTypeString,usageList,rc)
    
    
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

