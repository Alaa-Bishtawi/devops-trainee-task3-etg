from flask import Flask
import psutil # pip install psutil
import os.path
import metricsRetrival as metrics
import logging
from datetime import date

logging.basicConfig(filename='test.log',level=logging.DEBUG)

app = Flask(__name__)


# dictionary for messages
logMessage = {
    'default':'hello world route',
    'cpu_current_uasge':'cpu current usage is : {}%',
    'ram_current_usage':'ram current usage is : {}%',
    'hdd_current_usage':'hdd current  usage is : {}%',
    'hdd_day_usage':'hdd day usage is : {}%',
    'cpu_day_usage':'cpu day usage is : {}%',
    'ram_day_usage':'ram day uasge is : {}',
}

# default
@app.route('/log')
def log_world():
    f = open("test.log", "r")
    logfile = f.read()
    return logfile

@app.route('/')
def hello_world():
    
    today = date.today()
    logmessage=f'************* Time is {today}: #### "/" get request *************'
    
    logging.info(logmessage)
    return logMessage['default']

@app.route('/cpu_current_usage', methods=['GET'])
def cpu_current_usage():
    today = date.today()
    logmessage=f' ************* Time is {today}: #### "/cpu_current_usage" get request *************'
    logging.info(logmessage)
    return metrics.cpuCurrentRetrive()

@app.route('/ram_current_usage', methods=['GET'])
def ram_current_usage():
    today = date.today()
    logmessage=f'*************Time is {today}: #### "/ram_current_usage" get request *************'
    logging.info(logmessage)
    return metrics.ramCurrentRetrive()

# hdd current usage
@app.route('/hdd_current_usage', methods=['GET'])
def hdd_current_usage():
   today = date.today()
   logmessage=f'************* Time is {today}: #### "/hdd_current_usage" get request *************'
   logging.info(logmessage)
   return metrics.hddCurrentRetrive()


@app.route('/cpu_day_usage', methods=['GET'])
def cpy_day_usage():
    today = date.today()
    logmessage=f'************* Time is {today}: #### "/cpu_day_usage" get request *************'
    logging.info(logmessage)
    return metrics.cpuDayRetrive()

@app.route('/ram_day_usage', methods=['GET'])
def ram_day_usage():
    today = date.today()
    logmessage=f'*************Time is {today}: #### "/ram_day_usage" get request *************'
    logging.info(logmessage)
    return metrics.ramDayRetrive()

@app.route('/hdd_day_usage', methods=['GET'])
def hdd_day_usage():
    today = date.today()
    logmessage=f' *************Time is {today}: #### "/hdd_day_usage" get request *************'
    logging.info(logmessage)
    return metrics.hddDayRetrive()

if __name__ == '__main__':
        today = date.today()
        logmessage=f'*************Time is {today}: #### and server started *************'
        logging.info(logmessage)
        app.run(host='0.0.0.0', debug = True )
