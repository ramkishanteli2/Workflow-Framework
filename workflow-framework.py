import yaml
from yaml import Loader
import logging
import time
import threading

pathList = []


def path2String(pathList):
    return '.'.join(pathList)


def timeFunction(func_name, exe_time):
    time.sleep(int(exe_time))


def generateLogFile(data, key, isConcurrent=False):
    pathList.append(key)
    logging.warning(path2String(pathList) + " Entry")

    if(data['Type'] == 'Task'):

        if(data['Function'] == 'TimeFunction'):

            func_name = data['Inputs']['FunctionInput']
            exe_time = data['Inputs']['ExecutionTime']
            logging.warning(path2String(pathList) + " Executing " +
                            "TimeFunction " + "(" + func_name + ", " + exe_time + ")")
            if isConcurrent:
                t1 = threading.Thread()
                t1.start()
                timeFunction(func_name, exe_time)
            else:
                timeFunction(func_name, exe_time)
    elif (data['Type'] == 'Flow'):

        if(data['Execution'] == 'Sequential'):
            for activity in data['Activities']:
                generateLogFile(data['Activities'][activity], activity)

        elif(data['Execution'] == 'Concurrent'):
            for activity in data['Activities']:
                generateLogFile(data['Activities'][activity],
                                activity, isConcurrent=True)
    logging.warning(path2String(pathList) + " Exit")
    pathList.pop()


# Opening yaml file
with open("DataSet\Milestone1\Milestone1B.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Generating log files using data dictionary obtained from yaml file
logging.basicConfig(filename="logfile.txt", format="%(asctime)s.%(msecs)06d;%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S', filemode='w')

for workflow in data:
    generateLogFile(data[workflow], workflow)
