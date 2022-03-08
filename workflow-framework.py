import yaml
from yaml import Loader
import logging

pathList = []


def path2String(pathList):
    return '.'.join(pathList)


def timeFunction(func_name, exe_time):
    pass


def generateLogFile(data, key):
    pathList.append(key)
    logging.warning(path2String(pathList) + " Entry")

    if(data['Type'] == 'Task'):

        if(data['Function'] == 'TimeFunction'):

            func_name = data['Inputs']['FunctionInput']
            exe_time = data['Inputs']['ExecutionTime']
            logging.warning(path2String(pathList) + " Executing " +
                            "TimeFunction " + "(" + func_name + ", " + exe_time + ")")
            timeFunction(func_name, exe_time)

    elif (data['Type'] == 'Flow'):

        if(data['Execution'] == 'Sequential'):
            for activity in data['Activities']:
                generateLogFile(data['Activities'][activity], activity)

        elif(data['Execution'] == 'Concurrent'):
            # INCOMPLETE
            pass
    logging.warning(path2String(pathList) + " Exit")
    pathList.pop()


# Opening yaml file
yaml_file = open('DataSet\Milestone1/Milestone1A.yaml', mode='r')

# Reading data from yaml file
data = yaml.load(yaml_file, Loader=Loader)

# Generating log files using data dictionary obtained from yaml file
logging.basicConfig(filename="logfile.txt", format="%(asctime)s.%(msecs)06d;%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S', filemode='w')

print(data)
for workflow in data:
    generateLogFile(data[workflow], workflow)
