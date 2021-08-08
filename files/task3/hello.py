from flask import Flask
import psutil # pip install psutil
import os.path


import test2

# import auto
app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello World!'
#########################
#current reuest
@app.route('/cpu_current_usage', methods=['GET'])
def cpu_current_usage():
    a = str(psutil.cpu_percent())
    a = f"cpu current  usage is :{a}%"
  

    return a

@app.route('/ram_current_usage', methods=['GET'])
def ram_current_usage():
    ram = str(psutil.virtual_memory()[2])

    a = f"ram current  usage is :{ram}%"
   
    return a


@app.route('/hdd_current_usage', methods=['GET'])
def hdd_current_usage():
    hdd = psutil.disk_usage('/')
    hdd = hdd.used / (2 ** 30)
    hdd = str(hdd)
    
    a = f"hdd current  usage is :{hdd}%"

    return a

############################
#whole day request
@app.route('/hdd_day_usage', methods=['GET'])
def hdd_day_usage():
    # auto.db_creat()
    # auto.db_table_creat()
  
    return test2.hdd_retrive()

@app.route('/cpu_day_usage', methods=['GET'])
def cpy_day_usage():
    # auto.db_creat()
    # auto.db_table_creat()
    
    return test2.cpu_retrive()

@app.route('/ram_day_usage', methods=['GET'])
def ram_day_usage():
    # auto.db_creat()
    # auto.db_table_creat()
    
    a = test2.ram_retrive()
    return a
##################
if __name__ == '__main__':
        
       # auto.db_creat()
      #  auto.db_table_creat()
       

        app.run(host='0.0.0.0', debug = True )
    #app.run()